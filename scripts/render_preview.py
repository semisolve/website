"""Render theme-aware SVG previews from the published HEMT data (stdlib only)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / 'data/hemt_data.json').read_text())
X_MIN, X_MAX, Y_MIN, Y_MAX = 160, 225, -1.2, 1.8
LEFT, TOP, WIDTH, HEIGHT = 72, 28, 616, 294


def x_coord(x):
    return LEFT + (x - X_MIN) / (X_MAX - X_MIN) * WIDTH


def y_coord(y):
    return TOP + (Y_MAX - y) / (Y_MAX - Y_MIN) * HEIGHT


def render(theme):
    bg, ink, muted, grid = ('#ffffff', '#141414', '#707070', '#eeeeee') if theme == 'light' else ('#191919', '#f5f5f5', '#aaaaaa', '#303030')
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 450" role="img" aria-labelledby="title desc">',
           '<title id="title">AlGaN/GaN band structure and quantum confined states</title>',
           '<desc id="desc">Energy in eV against position in nm. Quantum and semiclassical band edges with three eigenstates. Squared wavefunctions are scaled and offset by their eigenenergies for display.</desc>',
           f'<rect width="720" height="450" fill="{bg}"/>',
           f'<defs><clipPath id="plot"><rect x="{LEFT}" y="{TOP}" width="{WIDTH}" height="{HEIGHT}"/></clipPath></defs>',
           f'<g font-family="Inter,Arial,sans-serif" font-size="15" fill="{muted}">']
    for x in range(160, 221, 10):
        sx = x_coord(x)
        svg.extend([f'<path d="M{sx:.2f} {TOP}v{HEIGHT}" stroke="{grid}"/>', f'<text x="{sx:.2f}" y="347" text-anchor="middle">{x}</text>'])
    for y in [-1, -.5, 0, .5, 1, 1.5]:
        sy = y_coord(y)
        svg.extend([f'<path d="M{LEFT} {sy:.2f}h{WIDTH}" stroke="{grid}"/>', f'<text x="59" y="{sy+5:.2f}" text-anchor="end">{y:g}</text>'])
    svg.extend(['<text x="380" y="374" text-anchor="middle">Position (nm)</text>', '<text transform="translate(22 175) rotate(-90)" text-anchor="middle">Energy (eV)</text>', '</g>'])
    scale = .35 / max(data['eigenvectors']['psi2_0'])
    traces = [
        ('Eꜰ', [0] * len(data['z']), muted, '2 5', 1),
        ('Ec (SC)', data['semiclassical']['Ec'], muted, '6 5', 1.5),
        ('Ev (SC)', data['semiclassical']['Ev'], muted, '9 4 2 4', 1.5),
        ('Ec', data['quantum']['Ec'], ink, '', 2.5),
        ('Ev', data['quantum']['Ev'], ink, '12 5', 2),
    ]
    for i, dash in enumerate(['6 4', '2 4', '8 4 2 4']):
        energy = data['eigenvalues'][i]
        values = [energy + value * scale for value in data['eigenvectors'][f'psi2_{i}']]
        traces.append((f'E{i+1} = {energy:.3f} eV', values, ink if i == 0 else muted, dash, 1.8))
    svg.append('<g clip-path="url(#plot)" fill="none">')
    for _, values, color, dash, width in traces:
        points = ' '.join(f'{x_coord(x):.2f},{y_coord(y):.2f}' for x, y in zip(data['z'], values))
        svg.append(f'<polyline points="{points}" stroke="{color}" stroke-width="{width}" stroke-dasharray="{dash}"/>')
    svg.append('</g>')
    # Compact, ordered key with explicit eigenenergies.
    for i, (name, _, color, dash, width) in enumerate(traces):
        x = 40 + (i % 4) * 170
        y = 403 + (i // 4) * 27
        svg.append(f'<path d="M{x} {y}h24" stroke="{color}" stroke-width="{width}" stroke-dasharray="{dash}"/>')
        svg.append(f'<text x="{x+32}" y="{y+5}" fill="{ink}" font-family="Inter,Arial,sans-serif" font-size="13">{name}</text>')
    svg.append('</svg>')
    (ROOT / f'images/hemt_preview_{theme}.svg').write_text('\n'.join(svg) + '\n')


if __name__ == '__main__':
    for theme in ['light', 'dark']:
        render(theme)
