import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib.utils import ImageReader
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, PageBreak, HRFlowable, Image,
                                 KeepTogether)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import ListFlowable, ListItem

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIAGRAM_DIR = os.path.join(BASE_DIR, 'diagrams')
OUTPUT_DIR = os.path.join(BASE_DIR, 'outputs')
os.makedirs(DIAGRAM_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ─────────────────────────── DIAGRAM HELPERS ────────────────────────────────

def save_fig(fig, name):
    path = os.path.join(DIAGRAM_DIR, f'{name}.png')
    fig.savefig(path, dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close(fig)
    return path


def make_diagram_double_integral_cartesian():
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5), facecolor='white')

    # LEFT: vertical strip (dy dx)
    ax = axes[0]
    ax.set_facecolor('white')
    x = np.linspace(0, 2, 300)
    f1 = 0.3 * x
    f2 = 0.5 * x + 0.6
    ax.fill_between(x, f1, f2, alpha=0.25, color='royalblue', label='Region R')
    ax.plot(x, f1, 'b-', lw=2, label=r'$y = f_1(x)$')
    ax.plot(x, f2, 'r-', lw=2, label=r'$y = f_2(x)$')
    xi = 1.2
    ax.axvline(xi, color='green', ls='--', lw=1.5)
    ax.annotate('', xy=(xi, 0.5*xi+0.6), xytext=(xi, 0.3*xi),
                arrowprops=dict(arrowstyle='<->', color='green', lw=1.5))
    ax.text(xi+0.05, 0.8, 'dy', color='green', fontsize=11, fontweight='bold')
    ax.axvline(0.4, color='grey', ls=':', lw=1)
    ax.axvline(1.9, color='grey', ls=':', lw=1)
    ax.text(0.35, -0.15, 'a', fontsize=11); ax.text(1.85, -0.15, 'b', fontsize=11)
    ax.set_title('Case (i): Vertical Strip  dy dx', fontsize=12, fontweight='bold', pad=8)
    ax.set_xlabel('x'); ax.set_ylabel('y')
    ax.legend(fontsize=9, loc='upper left')
    ax.set_xlim(-0.1, 2.3); ax.set_ylim(-0.3, 2)
    ax.spines['left'].set_position('zero'); ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_visible(False); ax.spines['top'].set_visible(False)

    # RIGHT: horizontal strip (dx dy)
    ax2 = axes[1]
    ax2.set_facecolor('white')
    y = np.linspace(0, 2, 300)
    g1 = 0.2 * y
    g2 = 0.4 * y + 0.5
    ax2.fill_betweenx(y, g1, g2, alpha=0.25, color='salmon', label='Region R')
    ax2.plot(g1, y, 'b-', lw=2, label=r'$x = f_1(y)$')
    ax2.plot(g2, y, 'r-', lw=2, label=r'$x = f_2(y)$')
    yi = 1.2
    ax2.axhline(yi, color='green', ls='--', lw=1.5)
    ax2.annotate('', xy=(0.4*yi+0.5, yi), xytext=(0.2*yi, yi),
                 arrowprops=dict(arrowstyle='<->', color='green', lw=1.5))
    ax2.text(0.55, yi+0.05, 'dx', color='green', fontsize=11, fontweight='bold')
    ax2.axhline(0.3, color='grey', ls=':', lw=1)
    ax2.axhline(1.9, color='grey', ls=':', lw=1)
    ax2.text(-0.2, 0.28, 'c', fontsize=11); ax2.text(-0.2, 1.88, 'd', fontsize=11)
    ax2.set_title('Case (ii): Horizontal Strip  dx dy', fontsize=12, fontweight='bold', pad=8)
    ax2.set_xlabel('x'); ax2.set_ylabel('y')
    ax2.legend(fontsize=9, loc='upper left')
    ax2.set_xlim(-0.3, 1.6); ax2.set_ylim(-0.3, 2.3)
    ax2.spines['left'].set_position('zero'); ax2.spines['bottom'].set_position('zero')
    ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False)

    fig.suptitle('Double Integration – Region of Integration (Cartesian)',
                 fontsize=13, fontweight='bold', y=1.01)
    fig.tight_layout()
    return save_fig(fig, 'double_cartesian')


def make_diagram_polar():
    fig, ax = plt.subplots(figsize=(5.5, 5), facecolor='white', subplot_kw={'projection': 'polar'})
    ax.set_facecolor('white')
    theta1, theta2 = np.pi/6, np.pi/2
    r1, r2 = 0.5, 1.4
    theta = np.linspace(theta1, theta2, 200)

    ax.fill_between(theta, r1, r2, alpha=0.3, color='royalblue')
    ax.plot([theta1, theta1], [r1, r2], 'b-', lw=2)
    ax.plot([theta2, theta2], [r1, r2], 'r-', lw=2)
    ax.plot(theta, [r1]*len(theta), 'g--', lw=2, label=r'$r = r_1(\theta)$')
    ax.plot(theta, [r2]*len(theta), 'm--', lw=2, label=r'$r = r_2(\theta)$')

    # wedge
    dtheta = 0.08
    tw = np.linspace(np.pi/3 - dtheta/2, np.pi/3 + dtheta/2, 50)
    ax.fill_between(tw, r1, r2, alpha=0.6, color='orange')
    ax.text(np.pi/3 + 0.1, 1.0, 'δθ', color='darkorange', fontsize=11, fontweight='bold')

    ax.set_title('Double Integration –\nPolar Co-ordinates', fontsize=12, fontweight='bold', pad=15)
    ax.set_thetalim(0, np.pi/2 + 0.2)
    mid = (theta1 + theta2) / 2
    ax.text(theta1 - 0.08, 1.8, r'$\theta_1$', fontsize=11, color='blue')
    ax.text(theta2 + 0.04, 1.8, r'$\theta_2$', fontsize=11, color='red')
    ax.legend(fontsize=9, loc='lower left', bbox_to_anchor=(0.0, -0.1))
    fig.tight_layout()
    return save_fig(fig, 'polar_double')


def make_diagram_change_of_order():
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5), facecolor='white')

    # Left: original order (y: x -> a, x: 0 -> a)
    ax = axes[0]
    ax.set_facecolor('white')
    a = 2.0
    x = np.linspace(0, a, 200)
    ax.fill_between(x, x, a, alpha=0.28, color='royalblue')
    ax.plot([0, a], [0, a], 'b-', lw=2, label='y = x')
    ax.axhline(a, color='r', lw=2, ls='--', label=f'y = a')
    ax.axvline(0, color='grey', lw=1)
    ax.axvline(a, color='grey', lw=1, ls=':')
    ax.annotate('', xy=(1.2, a), xytext=(1.2, 1.2),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))
    ax.text(1.28, 1.6, 'dy (inner)', color='green', fontsize=9)
    ax.set_title('Original Order: dy dx\n(y: x→a,  x: 0→a)', fontsize=11, fontweight='bold')
    ax.set_xlabel('x'); ax.set_ylabel('y')
    ax.legend(fontsize=9); ax.set_xlim(-0.2, 2.5); ax.set_ylim(-0.2, 2.5)
    ax.text(a+0.05, -0.15, 'a', fontsize=11); ax.text(-0.2, a, 'a', fontsize=11)
    ax.spines['left'].set_position('zero'); ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_visible(False); ax.spines['top'].set_visible(False)

    # Right: changed order (x: 0 -> y, y: 0 -> a)
    ax2 = axes[1]
    ax2.set_facecolor('white')
    y = np.linspace(0, a, 200)
    ax2.fill_between([0]*len(y), 0, y, alpha=0.28, color='salmon')  # placeholder
    ax2.fill_betweenx(y, 0, y, alpha=0.28, color='salmon')
    ax2.plot([0, a], [0, a], 'b-', lw=2, label='x = y')
    ax2.axhline(a, color='r', lw=2, ls='--', label='y = a')
    ax2.annotate('', xy=(0.8, 1.5), xytext=(0.0, 1.5),
                 arrowprops=dict(arrowstyle='->', color='purple', lw=2))
    ax2.text(0.1, 1.6, 'dx (inner)', color='purple', fontsize=9)
    ax2.set_title('Changed Order: dx dy\n(x: 0→y,  y: 0→a)', fontsize=11, fontweight='bold')
    ax2.set_xlabel('x'); ax2.set_ylabel('y')
    ax2.legend(fontsize=9); ax2.set_xlim(-0.2, 2.5); ax2.set_ylim(-0.2, 2.5)
    ax2.text(a+0.05, -0.15, 'a', fontsize=11); ax2.text(-0.2, a, 'a', fontsize=11)
    ax2.spines['left'].set_position('zero'); ax2.spines['bottom'].set_position('zero')
    ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False)

    fig.suptitle('Change of Order of Integration', fontsize=13, fontweight='bold', y=1.01)
    fig.tight_layout()
    return save_fig(fig, 'change_of_order')


def make_diagram_cardioid():
    fig, ax = plt.subplots(figsize=(5, 5), facecolor='white', subplot_kw={'projection': 'polar'})
    ax.set_facecolor('white')
    theta = np.linspace(0, 2*np.pi, 500)
    r_plus = 1 + np.cos(theta)
    r_minus = 1 - np.cos(theta)
    ax.fill(theta, r_plus, alpha=0.3, color='royalblue', label=r'$r=a(1+\cos\theta)$')
    ax.plot(theta, r_plus, 'b-', lw=2)
    ax.fill(theta, r_minus, alpha=0.3, color='salmon', label=r'$r=a(1-\cos\theta)$')
    ax.plot(theta, r_minus, 'r--', lw=2)
    ax.set_title('Cardioids', fontsize=13, fontweight='bold', pad=15)
    ax.legend(fontsize=9, loc='lower left', bbox_to_anchor=(-0.1, -0.15))
    fig.tight_layout()
    return save_fig(fig, 'cardioid')


def make_diagram_cartesian_to_polar():
    fig, ax = plt.subplots(figsize=(6, 5.5), facecolor='white')
    ax.set_facecolor('white')
    # Quarter circle
    theta = np.linspace(0, np.pi/2, 200)
    a = 2.0
    ax.fill_between(a*np.cos(theta), a*np.sin(theta), alpha=0.25, color='royalblue')
    ax.plot(a*np.cos(theta), a*np.sin(theta), 'b-', lw=2.5, label=r'$x^2+y^2=a^2$')
    ax.axvline(0, color='grey', lw=0.8)
    ax.axhline(0, color='grey', lw=0.8)
    # Radial strip
    th0 = np.pi/4
    ax.plot([0, a*np.cos(th0)], [0, a*np.sin(th0)], 'r-', lw=2, label='Radial strip r: 0→a')
    arc_t = np.linspace(0, np.pi/2, 100)
    ax.plot(0.4*np.cos(arc_t), 0.4*np.sin(arc_t), 'green', lw=1.5)
    ax.annotate('θ: 0 → π/2', xy=(0.5, 0.15), fontsize=10, color='green')
    ax.text(1.1, 1.1, 'r', fontsize=13, color='red', fontweight='bold')
    ax.set_xlim(-0.3, 2.6); ax.set_ylim(-0.3, 2.6)
    ax.set_xlabel('x  (= r cosθ)', fontsize=11)
    ax.set_ylabel('y  (= r sinθ)', fontsize=11)
    ax.set_title('Cartesian → Polar Transformation\n(Quarter Circle)', fontsize=12, fontweight='bold')
    ax.legend(fontsize=9)
    ax.text(0.05, -0.2, 'O', fontsize=11)
    ax.text(a+0.05, -0.2, 'a', fontsize=11)
    ax.text(-0.25, a+0.05, 'a', fontsize=11)
    ax.spines['right'].set_visible(False); ax.spines['top'].set_visible(False)
    fig.tight_layout()
    return save_fig(fig, 'cartesian_polar')


def make_diagram_triple():
    fig = plt.figure(figsize=(6, 5), facecolor='white')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('white')
    # Draw a sphere octant
    u = np.linspace(0, np.pi/2, 40)
    v = np.linspace(0, np.pi/2, 40)
    U, V = np.meshgrid(u, v)
    a = 1.5
    X = a * np.sin(U) * np.cos(V)
    Y = a * np.sin(U) * np.sin(V)
    Z = a * np.cos(U)
    ax.plot_surface(X, Y, Z, alpha=0.25, color='royalblue')
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    ax.set_title('Triple Integral – First Octant\nof Sphere x²+y²+z²=a²',
                 fontsize=11, fontweight='bold', pad=10)
    # Coordinate planes
    xx, yy = np.meshgrid(np.linspace(0, a, 5), np.linspace(0, a, 5))
    ax.plot_surface(xx, yy, xx*0, alpha=0.1, color='green')
    ax.set_xlim(0, a+0.2); ax.set_ylim(0, a+0.2); ax.set_zlim(0, a+0.2)
    fig.tight_layout()
    return save_fig(fig, 'triple_octant')


def make_diagram_cylindrical():
    fig = plt.figure(figsize=(5.5, 5), facecolor='white')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('white')
    # Cylinder x²+y²=1, z=0..2
    theta = np.linspace(0, 2*np.pi, 60)
    z = np.linspace(0, 2, 20)
    T, Z = np.meshgrid(theta, z)
    X = np.cos(T); Y = np.sin(T)
    ax.plot_surface(X, Y, Z, alpha=0.2, color='steelblue')
    # Top cap
    r = np.linspace(0, 1, 20)
    T2, R = np.meshgrid(theta, r)
    ax.plot_surface(R*np.cos(T2), R*np.sin(T2), T2*0+2, alpha=0.3, color='orange')
    ax.plot_surface(R*np.cos(T2), R*np.sin(T2), T2*0, alpha=0.3, color='green')
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    ax.set_title('Cylindrical Co-ordinates\nx²+y²=1', fontsize=11, fontweight='bold', pad=10)
    ax.text2D(0.05, 0.92, 'x = r cosθ,  y = r sinθ,  z = z', transform=ax.transAxes,
              fontsize=9, color='darkred')
    fig.tight_layout()
    return save_fig(fig, 'cylindrical')


def make_diagram_spherical():
    fig = plt.figure(figsize=(5.5, 5), facecolor='white')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('white')
    # Full sphere
    u = np.linspace(0, np.pi, 40)
    v = np.linspace(0, 2*np.pi, 40)
    U, V = np.meshgrid(u, v)
    a = 1.5
    X = a * np.sin(U) * np.cos(V)
    Y = a * np.sin(U) * np.sin(V)
    Z = a * np.cos(U)
    ax.plot_surface(X, Y, Z, alpha=0.15, color='royalblue')
    # Axes lines
    ax.quiver(0,0,0, 2,0,0, color='red', arrow_length_ratio=0.15)
    ax.quiver(0,0,0, 0,2,0, color='green', arrow_length_ratio=0.15)
    ax.quiver(0,0,0, 0,0,2, color='blue', arrow_length_ratio=0.15)
    # r vector
    r0 = np.array([0.9, 0.7, 1.0])
    ax.quiver(0,0,0, *r0, color='black', lw=2, arrow_length_ratio=0.1)
    ax.text(*r0, ' r', fontsize=12, color='black', fontweight='bold')
    ax.text(2.1,0,0,'X', fontsize=10, color='red')
    ax.text(0,2.1,0,'Y', fontsize=10, color='green')
    ax.text(0,0,2.1,'Z', fontsize=10, color='blue')
    ax.set_title('Spherical Polar Co-ordinates\nx=r sinθ cosφ,  y=r sinθ sinφ,  z=r cosθ',
                 fontsize=10, fontweight='bold', pad=10)
    ax.set_xlim(-2,2); ax.set_ylim(-2,2); ax.set_zlim(-2,2)
    ax.axis('off')
    fig.tight_layout()
    return save_fig(fig, 'spherical')


def make_diagram_area_parabola():
    fig, ax = plt.subplots(figsize=(5.5, 5), facecolor='white')
    ax.set_facecolor('white')
    x = np.linspace(0, 1, 300)
    y1 = 2 * x**2    # parabola y=2x²
    y2 = 2 * np.sqrt(x)  # from y²=4x => y=2√x
    ax.fill_between(x, y1, y2, alpha=0.3, color='royalblue', label='Enclosed Area')
    ax.plot(x, y1, 'b-', lw=2.5, label=r'$y = 2x^2$')
    ax.plot(x, y2, 'r-', lw=2.5, label=r'$y^2 = 4x \Rightarrow y = 2\sqrt{x}$')
    ax.plot([0, 1], [0, 0], 'k-', lw=0.8)
    ax.scatter([0, 1], [0, 2], color='black', zorder=5)
    ax.text(-0.05, -0.1, '(0,0)', fontsize=9)
    ax.text(1.02, 2.0, '(1,2)', fontsize=9)
    ax.set_title('Area Enclosed by\ny = 2x² and y² = 4x', fontsize=12, fontweight='bold')
    ax.set_xlabel('x'); ax.set_ylabel('y')
    ax.legend(fontsize=9)
    ax.spines['right'].set_visible(False); ax.spines['top'].set_visible(False)
    fig.tight_layout()
    return save_fig(fig, 'area_parabola')


# ─────────────────────────── GENERATE ALL DIAGRAMS ──────────────────────────

print("Generating diagrams...")
d_cart   = make_diagram_double_integral_cartesian()
d_polar  = make_diagram_polar()
d_order  = make_diagram_change_of_order()
d_card   = make_diagram_cardioid()
d_cp     = make_diagram_cartesian_to_polar()
d_tri    = make_diagram_triple()
d_cyl    = make_diagram_cylindrical()
d_sph    = make_diagram_spherical()
d_area   = make_diagram_area_parabola()
print("Diagrams done.")

# ─────────────────────────── STYLES ─────────────────────────────────────────

PAGE_W, PAGE_H = A4
MARGIN = 1.8 * cm

doc = SimpleDocTemplate(
    os.path.join(OUTPUT_DIR, 'MSBTE_Multiple_Integrals_Guide.pdf'),
    pagesize=A4,
    leftMargin=MARGIN, rightMargin=MARGIN,
    topMargin=2 * cm, bottomMargin=2 * cm
)

styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle('GuideTitle', parent=styles['Title'],
    fontSize=22, textColor=colors.HexColor('#1a237e'),
    spaceAfter=6, alignment=TA_CENTER, fontName='Helvetica-Bold')

subtitle_style = ParagraphStyle('Subtitle', parent=styles['Normal'],
    fontSize=13, textColor=colors.HexColor('#37474f'),
    spaceAfter=4, alignment=TA_CENTER, fontName='Helvetica')

unit_style = ParagraphStyle('UnitHead', parent=styles['Heading1'],
    fontSize=17, textColor=colors.white,
    backColor=colors.HexColor('#1a237e'), spaceAfter=12,
    spaceBefore=18, fontName='Helvetica-Bold', leading=22,
    leftIndent=-0.5*cm, rightIndent=-0.5*cm,
    borderPadding=(6,10,6,10))

section_style = ParagraphStyle('SectionHead', parent=styles['Heading2'],
    fontSize=13, textColor=colors.HexColor('#0d47a1'),
    spaceBefore=14, spaceAfter=6, fontName='Helvetica-Bold',
    borderPad=2, leftIndent=0,
    borderColor=colors.HexColor('#0d47a1'))

subsection_style = ParagraphStyle('SubSection', parent=styles['Heading3'],
    fontSize=11, textColor=colors.HexColor('#1565c0'),
    spaceBefore=10, spaceAfter=4, fontName='Helvetica-Bold')

body_style = ParagraphStyle('Body', parent=styles['Normal'],
    fontSize=10.5, leading=16, spaceAfter=6,
    alignment=TA_JUSTIFY, fontName='Helvetica')

bullet_style = ParagraphStyle('Bullet', parent=styles['Normal'],
    fontSize=10.5, leading=15, spaceAfter=4, leftIndent=18,
    fontName='Helvetica', firstLineIndent=-14)

formula_style = ParagraphStyle('Formula', parent=styles['Normal'],
    fontSize=11, leading=18, spaceAfter=6, spaceBefore=6,
    backColor=colors.HexColor('#e8eaf6'), alignment=TA_CENTER,
    borderPadding=(8, 12, 8, 12), fontName='Helvetica-Bold',
    textColor=colors.HexColor('#1a237e'))

note_style = ParagraphStyle('Note', parent=styles['Normal'],
    fontSize=10, leading=14, spaceAfter=6, spaceBefore=4,
    backColor=colors.HexColor('#fff8e1'),
    borderPadding=(6, 10, 6, 10), fontName='Helvetica',
    textColor=colors.HexColor('#4e342e'), leftIndent=10, rightIndent=10)

keyword_style = ParagraphStyle('Keyword', parent=styles['Normal'],
    fontSize=10.5, leading=15, spaceAfter=4, leftIndent=18,
    fontName='Helvetica-Bold', textColor=colors.HexColor('#880e4f'),
    firstLineIndent=-14)

example_style = ParagraphStyle('Example', parent=styles['Normal'],
    fontSize=10, leading=15, spaceAfter=4, spaceBefore=6,
    backColor=colors.HexColor('#f1f8e9'),
    borderPadding=(6, 10, 6, 10), fontName='Helvetica',
    textColor=colors.HexColor('#1b5e20'), leftIndent=10, rightIndent=10)

step_style = ParagraphStyle('Step', parent=styles['Normal'],
    fontSize=10.5, leading=15, spaceAfter=4, leftIndent=20,
    fontName='Helvetica', firstLineIndent=-16)

warning_style = ParagraphStyle('Warning', parent=styles['Normal'],
    fontSize=10, leading=14, spaceAfter=6, spaceBefore=4,
    backColor=colors.HexColor('#ffebee'),
    borderPadding=(6, 10, 6, 10), fontName='Helvetica',
    textColor=colors.HexColor('#b71c1c'), leftIndent=10, rightIndent=10)

def B(text): return f'<b>{text}</b>'
def I(text): return f'<i>{text}</i>'
def C(text, col='#880e4f'): return f'<font color="{col}"><b>{text}</b></font>'

def bullet(text, style=bullet_style):
    return Paragraph(f'• {text}', style)

def numbered(n, text):
    return Paragraph(f'<b>{n}.</b>  {text}', step_style)

def formula(text):
    return Paragraph(text, formula_style)

def note(text):
    return Paragraph(f'<b>📝 Note:</b>  {text}', note_style)

def example_block(text):
    return Paragraph(f'<b>✏ Example:</b>  {text}', example_style)

def warn(text):
    return Paragraph(f'<b>⚠ Important:</b>  {text}', warning_style)

def keyword(text):
    return Paragraph(f'★  {text}', keyword_style)

def section_line():
    return HRFlowable(width='100%', thickness=1, color=colors.HexColor('#90caf9'),
                      spaceBefore=6, spaceAfter=6)

def img(path, width=14*cm, max_height=8.5*cm):
    reader = ImageReader(path)
    src_w, src_h = reader.getSize()
    if src_w <= 0 or src_h <= 0:
        return Image(path, width=width, height=max_height)

    scale = min(width / src_w, max_height / src_h)
    draw_w = src_w * scale
    draw_h = src_h * scale
    return Image(path, width=draw_w, height=draw_h)

# ─────────────────────────── BUILD CONTENT ──────────────────────────────────

story = []

# ════════════════════════════════════════════════
#                   COVER PAGE
# ════════════════════════════════════════════════

story.append(Spacer(1, 1.5*cm))

# Top banner table
banner_data = [['MSBTE K-SCHEME  |  ENGINEERING MATHEMATICS – II']]
banner_table = Table(banner_data, colWidths=[PAGE_W - 2*MARGIN])
banner_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#1a237e')),
    ('TEXTCOLOR', (0,0), (-1,-1), colors.white),
    ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 13),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
]))
story.append(banner_table)
story.append(Spacer(1, 0.6*cm))

story.append(Paragraph('UNIT – IV', ParagraphStyle('CoverUnit',
    parent=styles['Normal'], fontSize=16, alignment=TA_CENTER,
    textColor=colors.HexColor('#0d47a1'), fontName='Helvetica-Bold')))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph('MULTIPLE INTEGRALS', ParagraphStyle('CoverTitle',
    parent=styles['Normal'], fontSize=32, alignment=TA_CENTER,
    textColor=colors.HexColor('#1a237e'), fontName='Helvetica-Bold', leading=38)))
story.append(Spacer(1, 0.4*cm))

story.append(Paragraph('Complete Exam Guide with Theory, Formulas, Diagrams & Solved Examples',
    ParagraphStyle('CoverSub', parent=styles['Normal'], fontSize=13,
    alignment=TA_CENTER, textColor=colors.HexColor('#37474f'),
    fontName='Helvetica', leading=18)))

story.append(Spacer(1, 0.8*cm))
story.append(HRFlowable(width='100%', thickness=2, color=colors.HexColor('#1a237e')))
story.append(Spacer(1, 0.5*cm))

# Topics covered
topics_data = [
    ['TOPICS COVERED IN THIS GUIDE'],
    ['4.1  Introduction to Multiple Integrals'],
    ['4.2  Double Integration – Cartesian Co-ordinates'],
    ['4.3  Double Integration – Polar Co-ordinates'],
    ['4.4  Change of Order of Integration'],
    ['4.5  Area Enclosed by Plane Curves (Cartesian)'],
    ['4.6  Area Enclosed by Plane Curves (Polar)'],
    ['4.7  Triple Integrals'],
    ['4.8  Volume of Solids using Triple Integrals'],
    ['4.9  Change of Variables (Cartesian ↔ Polar, Cylindrical, Spherical)'],
]
t = Table(topics_data, colWidths=[PAGE_W - 2*MARGIN])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0d47a1')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#e8eaf6')),
    ('TEXTCOLOR', (0,1), (-1,-1), colors.HexColor('#1a237e')),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,0), 12),
    ('FONTSIZE', (0,1), (-1,-1), 11),
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 7),
    ('BOTTOMPADDING', (0,0), (-1,-1), 7),
    ('LEFTPADDING', (0,0), (-1,0), 15),
    ('LEFTPADDING', (0,1), (-1,-1), 30),
    ('LINEBELOW', (0,0), (-1,-1), 0.5, colors.HexColor('#9fa8da')),
    ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#1a237e')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#e8eaf6'), colors.HexColor('#f5f5ff')]),
]))
story.append(t)

story.append(Spacer(1, 0.8*cm))
story.append(HRFlowable(width='100%', thickness=2, color=colors.HexColor('#1a237e')))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph('Prepared for MSBTE K-Scheme Students | Exam Ready Reference',
    ParagraphStyle('CoverBottom', parent=styles['Normal'], fontSize=10,
    alignment=TA_CENTER, textColor=colors.HexColor('#546e7a'), fontName='Helvetica-Oblique')))

story.append(PageBreak())

# ════════════════════════════════════════════════
#   4.1  INTRODUCTION
# ════════════════════════════════════════════════

story.append(Paragraph('4.1  Introduction to Multiple Integrals', unit_style))
story.append(Spacer(1, 0.2*cm))

story.append(Paragraph(
    'In Engineering Mathematics, we often deal with functions that depend on '
    '<b>more than one variable</b> — for example, area, volume, mass, and centre '
    'of gravity all require integration over two or three dimensions. '
    'Multiple integrals are a systematic way to perform such integrations.',
    body_style))

story.append(Paragraph(
    'When a physical quantity is spread over a region in 2D or 3D space, we '
    'cannot compute it with a single integral. We need to integrate over '
    '<b>two variables simultaneously</b> (Double Integral) or '
    '<b>three variables simultaneously</b> (Triple Integral).',
    body_style))

story.append(Spacer(1, 0.2*cm))
story.append(Paragraph('Key Keywords', section_style))
story.append(section_line())

kws = [
    (C('Double Integral'), 'Integration over a 2D region R; denoted ∬f(x,y) dA.'),
    (C('Triple Integral'), 'Integration over a 3D volume V; denoted ∭f(x,y,z) dV.'),
    (C('Region of Integration'), 'The 2D or 3D domain over which integration is performed.'),
    (C('Iterated Integral'), 'A double/triple integral evaluated step-by-step, one variable at a time.'),
    (C('Limits of Integration'), 'The boundary values of each variable — can be constants or functions.'),
    (C('Cartesian Co-ordinates'), 'Standard x-y (or x-y-z) system for expressing regions.'),
    (C('Polar Co-ordinates'), 'System using (r, θ) — useful for circular/symmetric regions.'),
    (C('Change of Order'), 'Reversing the order of integration to simplify evaluation.'),
]

for kw, defn in kws:
    story.append(Paragraph(f'★  {kw} — {defn}', bullet_style))

story.append(Spacer(1, 0.2*cm))
story.append(note('Every double integral can be viewed as a limit of a double sum — '
                  'just like a single integral is the limit of a Riemann sum.'))

story.append(PageBreak())

# ════════════════════════════════════════════════
#   4.2  DOUBLE INTEGRATION – CARTESIAN
# ════════════════════════════════════════════════

story.append(Paragraph('4.2  Double Integration in Cartesian Co-ordinates', unit_style))
story.append(Spacer(1, 0.2*cm))

story.append(Paragraph('What is a Double Integral?', section_style))
story.append(section_line())

story.append(Paragraph(
    'Let f(x, y) be a continuous function defined over a closed region R. '
    'We divide R into n small sub-regions of areas A₁, A₂, …, Aₙ, pick any '
    'point (xᵢ, yⱼ) inside each sub-region, and form the sum '
    'Σ f(xᵢ, yⱼ) Aᵢ. As n → ∞ and each area Aᵢ → 0, this sum converges '
    'to the <b>Double Integral</b>:', body_style))

story.append(formula('∬_R f(x, y) dA  =  lim_(n→∞)  Σ f(xᵢ, yⱼ) Aᵢ'))

story.append(Paragraph(
    'In practice, the double integral is written as an <b>iterated integral</b> '
    'and evaluated by performing two successive single integrations:',
    body_style))

story.append(formula('∫∫ f(x, y) dy dx   or   ∫∫ f(x, y) dx dy'))

story.append(Spacer(1, 0.2*cm))
story.append(Paragraph('How to Evaluate a Double Integral', section_style))
story.append(section_line())

steps_eval = [
    ('Step 1', 'Start with the <b>inner integral</b>. Integrate f(x, y) with respect to the inner variable (say y), treating the outer variable (x) as a <b>constant</b>.'),
    ('Step 2', 'Substitute the <b>inner limits</b> to get a function of the outer variable only.'),
    ('Step 3', 'Integrate the result with respect to the <b>outer variable</b> between the outer limits.'),
    ('Step 4', 'Substitute the outer limits to get the <b>final numerical answer</b>.'),
]
for s, t in steps_eval:
    story.append(Paragraph(f'<b>{s}:</b>  {t}', step_style))

story.append(Spacer(1, 0.3*cm))
story.append(Paragraph('Region of Integration – Two Cases', section_style))
story.append(section_line())

story.append(Paragraph(
    'The shape of the region R determines how we set up the limits. '
    'There are <b>two standard cases</b>:', body_style))

# Case descriptions
case_data = [
    ['Case', 'Integral Form', 'Strip Type', 'y-limits', 'x-limits'],
    ['(i)',  '∫_a^b ∫_{f₁(x)}^{f₂(x)} f dy dx',
     'Vertical strip', 'y = f₁(x)  to  y = f₂(x)', 'x = a  to  x = b'],
    ['(ii)', '∫_c^d ∫_{g₁(y)}^{g₂(y)} f dx dy',
     'Horizontal strip', 'y = c  to  y = d', 'x = g₁(y)  to  x = g₂(y)'],
]
t = Table(case_data, colWidths=[1.5*cm, 5*cm, 3*cm, 4*cm, 3*cm])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a237e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9.5),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#e8eaf6'), colors.HexColor('#f5f5ff')]),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9fa8da')),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
]))
story.append(t)
story.append(Spacer(1, 0.3*cm))

story.append(img(d_cart, width=15*cm))
story.append(Paragraph(
    '<i>Figure 4.1 — Left: Vertical strips for dy dx order. '
    'Right: Horizontal strips for dx dy order.</i>',
    ParagraphStyle('Caption', parent=styles['Normal'], fontSize=9,
                   alignment=TA_CENTER, textColor=colors.grey)))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph('Important Rule About Correct Form', section_style))
story.append(section_line())

story.append(warn(
    'If the limits of the <b>inner integral are functions of x</b>, '
    'then the first integration must be <b>with respect to y</b>. '
    'If the limits of the inner integral are functions of y, '
    'the first integration must be with respect to x. '
    'Always check the correct form before evaluating!'))

story.append(Spacer(1, 0.2*cm))
story.append(Paragraph('Key Formulas', section_style))
story.append(section_line())

formulas_cart = [
    ('Standard Double Integral',
     '∫_a^b ∫_{f₁(x)}^{f₂(x)} f(x,y) dy dx'),
    ('When limits are constants',
     '∫_a^b ∫_c^d f(x,y) dy dx  =  [∫_c^d f(x,y) dy] evaluated from a to b'),
    ('Separable functions',
     '∫_a^b ∫_c^d f(x)·g(y) dy dx  =  [∫_a^b f(x) dx] × [∫_c^d g(y) dy]'),
]
for name, frm in formulas_cart:
    story.append(Paragraph(f'<b>{name}:</b>', subsection_style))
    story.append(formula(frm))

story.append(Spacer(1, 0.3*cm))
story.append(Paragraph('Solved Examples', section_style))
story.append(section_line())

ex1 = [
    example_block('Evaluate ∫₀¹ ∫₁² x(x+y) dy dx'),
    Paragraph('<b>Solution:</b>', subsection_style),
    Paragraph('Inner integration (w.r.t. y, treating x as constant):', body_style),
    formula('∫₁² x(x+y) dy  =  [x²y + xy²/2]₁²  =  (2x² + 2x) − (x² + x/2)  =  x² + 3x/2'),
    Paragraph('Outer integration (w.r.t. x):', body_style),
    formula('∫₀¹ (x² + 3x/2) dx  =  [x³/3 + 3x²/4]₀¹  =  1/3 + 3/4  =  13/12'),
    Paragraph('<b>Answer: 13/12</b>', ParagraphStyle('Ans', parent=styles['Normal'],
        fontSize=11, fontName='Helvetica-Bold', textColor=colors.HexColor('#1b5e20'))),
]
for el in ex1: story.append(el)
story.append(Spacer(1, 0.2*cm))

ex2_items = [
    example_block('Evaluate ∫₀ᵃ ∫₀ᵇ xy(x−y) dy dx'),
    Paragraph('<b>Solution:</b>', subsection_style),
    Paragraph('Inner integration (w.r.t. y):', body_style),
    formula('∫₀ᵇ (x²y − xy²) dy  =  [x²y²/2 − xy³/3]₀ᵇ  =  b²x²/2 − b³x/3'),
    Paragraph('Outer integration (w.r.t. x):', body_style),
    formula('∫₀ᵃ (b²x²/2 − b³x/3) dx  =  [b²x³/6 − b³x²/6]₀ᵃ  =  a³b²/6 − a²b³/6'),
    Paragraph('<b>Answer: (a²b²/6)(a − b)</b>', ParagraphStyle('Ans', parent=styles['Normal'],
        fontSize=11, fontName='Helvetica-Bold', textColor=colors.HexColor('#1b5e20'))),
]
for el in ex2_items: story.append(el)
story.append(Spacer(1, 0.2*cm))

ex3_items = [
    example_block('Evaluate ∫₀³ ∫₀² eˣ⁺ʸ dy dx'),
    Paragraph('<b>Solution (Separable):</b>', subsection_style),
    Paragraph('Since e^(x+y) = eˣ · eʸ, the function is separable:', body_style),
    formula('∫₀³ ∫₀² eˣ⁺ʸ dy dx  =  [∫₀³ eˣ dx] × [∫₀² eʸ dy]'),
    formula('=  [eˣ]₀³ × [eʸ]₀²  =  (e³ − 1)(e² − 1)'),
    Paragraph('<b>Answer: (e³ − 1)(e² − 1)</b>', ParagraphStyle('Ans', parent=styles['Normal'],
        fontSize=11, fontName='Helvetica-Bold', textColor=colors.HexColor('#1b5e20'))),
]
for el in ex3_items: story.append(el)

story.append(PageBreak())

# ════════════════════════════════════════════════
#   4.3  DOUBLE INTEGRATION – POLAR
# ════════════════════════════════════════════════

story.append(Paragraph('4.3  Double Integration in Polar Co-ordinates', unit_style))
story.append(Spacer(1, 0.2*cm))

story.append(Paragraph('Why Polar Co-ordinates?', section_style))
story.append(section_line())

story.append(Paragraph(
    'When the region of integration is <b>circular, annular, or has angular symmetry</b>, '
    'expressing the integral in Cartesian form becomes very complicated. '
    'In such situations, <b>Polar Co-ordinates</b> make the limits much simpler '
    'and the integral easier to evaluate.', body_style))

story.append(Paragraph('Standard Form of Polar Double Integral', section_style))
story.append(section_line())

story.append(formula('∫_{θ₁}^{θ₂} ∫_{r₁(θ)}^{r₂(θ)} f(r, θ) r dr dθ'))

story.append(Paragraph(
    'The extra factor <b>"r"</b> in the integrand comes from the Jacobian of '
    'the polar transformation. It is <b>always required</b> when converting from '
    'Cartesian to Polar form.', body_style))

story.append(Spacer(1, 0.2*cm))
story.append(img(d_polar, width=10*cm))
story.append(Paragraph(
    '<i>Figure 4.2 — Region bounded by r₁(θ) ≤ r ≤ r₂(θ) and θ₁ ≤ θ ≤ θ₂. '
    'PQ is a wedge of angular thickness δθ.</i>',
    ParagraphStyle('Caption', parent=styles['Normal'], fontSize=9,
                   alignment=TA_CENTER, textColor=colors.grey)))

story.append(Spacer(1, 0.3*cm))
story.append(Paragraph('How to Evaluate a Polar Double Integral', section_style))
story.append(section_line())

polar_steps = [
    ('Step 1', 'Write limits: θ varies between two angles (θ₁ and θ₂), and r varies between two curves r₁(θ) and r₂(θ).'),
    ('Step 2', 'Integrate f(r, θ) · r with respect to r first (inner integral), treating θ as constant.'),
    ('Step 3', 'Integrate the resulting function with respect to θ (outer integral).'),
]
for s, t in polar_steps:
    story.append(Paragraph(f'<b>{s}:</b>  {t}', step_style))

story.append(Spacer(1, 0.3*cm))
story.append(Paragraph('Key Formulas Used in Polar Integration', section_style))
story.append(section_line())

polar_formulas = [
    ('Walli\'s Formula – sin²θ or cos²θ',
     '∫₀^(π/2) sin²θ dθ  =  ∫₀^(π/2) cos²θ dθ  =  (1/2)·(π/2)'),
    ('Walli\'s Formula – cos³θ or sin³θ',
     '∫₀^(π/2) cos³θ dθ  =  ∫₀^(π/2) sin³θ dθ  =  (2/3)'),
    ('Walli\'s Formula – cos⁴θ',
     '∫₀^(π/2) cos⁴θ dθ  =  (3/4)·(1/2)·(π/2)'),
    ('Symmetry shortcut',
     '∫₋ᵅᵅ f(θ) dθ  =  2 ∫₀ᵅ f(θ) dθ   (when f is even in θ)'),
]
for name, frm in polar_formulas:
    story.append(Paragraph(f'<b>{name}:</b>', subsection_style))
    story.append(formula(frm))

story.append(Spacer(1, 0.3*cm))
story.append(Paragraph('Solved Examples', section_style))
story.append(section_line())

pex1 = [
    example_block('Evaluate ∫₀^(π/2) ∫₀^(sinθ) r dr dθ'),
    Paragraph('<b>Solution:</b>', subsection_style),
    formula('Inner: ∫₀^(sinθ) r dr  =  [r²/2]₀^(sinθ)  =  sin²θ/2'),
    formula('Outer: ∫₀^(π/2) sin²θ/2 dθ  =  (1/2)·(1/2)·(π/2)  =  π/8'),
    Paragraph('<b>Answer: π/8</b>', ParagraphStyle('Ans', parent=styles['Normal'],
        fontSize=11, fontName='Helvetica-Bold', textColor=colors.HexColor('#1b5e20'))),
]
for el in pex1: story.append(el)
story.append(Spacer(1, 0.2*cm))

pex2 = [
    example_block('Evaluate ∫₀^(π) ∫₀^(sinθ) r dr dθ'),
    Paragraph('<b>Solution:</b>', subsection_style),
    formula('Inner: ∫₀^(sinθ) r dr  =  sin²θ/2'),
    formula('Outer: ∫₀^π sin²θ/2 dθ  =  (1/2)·∫₀^π (1−cos2θ)/2 dθ  =  π/4'),
    Paragraph('<b>Answer: π/4</b>', ParagraphStyle('Ans', parent=styles['Normal'],
        fontSize=11, fontName='Helvetica-Bold', textColor=colors.HexColor('#1b5e20'))),
]
for el in pex2: story.append(el)

story.append(PageBreak())

# ════════════════════════════════════════════════
#   4.4  CHANGE OF ORDER OF INTEGRATION
# ════════════════════════════════════════════════

story.append(Paragraph('4.4  Change of Order of Integration', unit_style))
story.append(Spacer(1, 0.2*cm))

story.append(Paragraph('Why Change the Order?', section_style))
story.append(section_line())

story.append(Paragraph(
    'Sometimes the given integral is <b>difficult or impossible to evaluate</b> '
    'in the given order of integration. By changing the order (from dy dx to dx dy, '
    'or vice versa), we often get a simpler integral that can be evaluated easily. '
    'This technique is called the <b>Change of Order of Integration</b>.', body_style))

story.append(Paragraph('Step-by-Step Working Rule', section_style))
story.append(section_line())

co_steps = [
    ('Step 1', '<b>Identify the given order</b> of integration (dy dx or dx dy).'),
    ('Step 2', '<b>Write the equations</b> corresponding to the given limits (e.g., y = x, y = a, x = 0, x = a).'),
    ('Step 3', '<b>Sketch the region of integration</b> by plotting these boundary curves and lines.'),
    ('Step 4', '<b>Choose the new order</b> of integration. If the original was dy dx, the new order will be dx dy, and vice versa.'),
    ('Step 5', '<b>Draw the appropriate strip</b>: vertical strip for dy dx, horizontal strip for dx dy.'),
    ('Step 6', '<b>Determine the new limits</b> by reading off the strip from the region diagram.'),
    ('Step 7', '<b>Evaluate the integral</b> with the new limits.'),
]
for s, t in co_steps:
    story.append(Paragraph(f'<b>{s}:</b>  {t}', step_style))

story.append(Spacer(1, 0.3*cm))
story.append(img(d_order, width=15*cm))
story.append(Paragraph(
    '<i>Figure 4.3 — Change of order: original dy dx (left) changed to dx dy (right). '
    'The shaded region R is the same — only the strip direction changes.</i>',
    ParagraphStyle('Caption', parent=styles['Normal'], fontSize=9,
                   alignment=TA_CENTER, textColor=colors.grey)))

story.append(Spacer(1, 0.3*cm))
story.append(Paragraph('When the Region Splits into Two Parts', section_style))
story.append(section_line())

story.append(Paragraph(
    'Sometimes, after changing the order, the region R cannot be described '
    'by a single set of limits. In such cases, <b>divide the region into two '
    'sub-regions R₁ and R₂</b>, evaluate the integral over each sub-region '
    'separately, and add the results.', body_style))

story.append(formula('∬_R f dA  =  ∬_{R₁} f dA  +  ∬_{R₂} f dA'))

story.append(Spacer(1, 0.3*cm))
story.append(Paragraph('Solved Examples', section_style))
story.append(section_line())

coex1 = [
    example_block('Change the order of integration in ∫₀ᵃ ∫ₓᵃ f(x,y) dy dx, then write the new integral.'),
    Paragraph('<b>Solution:</b>', subsection_style),
    bullet('Given limits: y: x → a,  x: 0 → a'),
    bullet('Boundary curves: y = x, y = a, x = 0, x = a'),
    bullet('The region R is the triangle above the line y = x, below y = a, for 0 ≤ x ≤ a.'),
    bullet('For the changed order dx dy: the strip is horizontal → x: 0 → y,  y: 0 → a'),
    formula('Changed Integral: ∫₀ᵃ ∫₀ʸ f(x,y) dx dy'),
]
for el in coex1: story.append(el)

story.append(Spacer(1, 0.2*cm))

coex2 = [
    example_block('Change order and evaluate ∫₀ᵃ ∫ₓᵃ (x²+y²) dy dx'),
    Paragraph('<b>Solution (using result above):</b>', subsection_style),
    Paragraph('Changed integral: ∫₀ᵃ ∫₀ʸ (x²+y²) dx dy', body_style),
    formula('∫₀ʸ (x²+y²) dx  =  [x³/3 + y²x]₀ʸ  =  y³/3 + y³  =  4y³/3'),
    formula('∫₀ᵃ (4y³/3) dy  =  [y⁴/3]₀ᵃ  =  a⁴/3'),
    Paragraph('<b>Answer: a⁴/3</b>', ParagraphStyle('Ans', parent=styles['Normal'],
        fontSize=11, fontName='Helvetica-Bold', textColor=colors.HexColor('#1b5e20'))),
]
for el in coex2: story.append(el)

story.append(Spacer(1, 0.2*cm))

coex3 = [
    example_block('Change order and evaluate ∫₀^∞ ∫ₓ^∞ (e⁻ʸ/y) dy dx'),
    Paragraph('<b>Solution:</b>', subsection_style),
    bullet('Given: y: x → ∞,  x: 0 → ∞'),
    bullet('Region: above the line y = x in the first quadrant (y ≥ x, x ≥ 0)'),
    bullet('Changed order dx dy: x: 0 → y,  y: 0 → ∞'),
    formula('∫₀^∞ ∫₀ʸ (e⁻ʸ/y) dx dy  =  ∫₀^∞ e⁻ʸ/y · [x]₀ʸ dy  =  ∫₀^∞ e⁻ʸ dy  =  1'),
    Paragraph('<b>Answer: 1</b>', ParagraphStyle('Ans', parent=styles['Normal'],
        fontSize=11, fontName='Helvetica-Bold', textColor=colors.HexColor('#1b5e20'))),
]
for el in coex3: story.append(el)

story.append(PageBreak())

# ════════════════════════════════════════════════
#   4.5  AREA – CARTESIAN
# ════════════════════════════════════════════════

story.append(Paragraph('4.5  Area Enclosed by Plane Curves (Cartesian)', unit_style))
story.append(Spacer(1, 0.2*cm))

story.append(Paragraph('Concept', section_style))
story.append(section_line())

story.append(Paragraph(
    'The area of a region R in the xy-plane can be computed directly using '
    'a double integral. We integrate the function f(x,y) = 1 over the region R. '
    'Each small element of area dA contributes 1 × dA = dA to the total area.', body_style))

story.append(Paragraph('Fundamental Area Formulas', section_style))
story.append(section_line())

story.append(formula('Area  =  ∬_R dA  =  ∬_R dy dx   (or)   ∬_R dx dy'))
story.append(Spacer(1, 0.1*cm))
story.append(formula('Area (Cartesian)  =  ∫_a^b ∫_{f₁(x)}^{f₂(x)} dy dx  =  ∫_a^b [f₂(x) − f₁(x)] dx'))

story.append(Spacer(1, 0.2*cm))
story.append(Paragraph('How to Find Area Using Double Integration', section_style))
story.append(section_line())

area_steps = [
    ('Step 1', 'Find intersection points of the given curves to determine limits.'),
    ('Step 2', 'Decide which curve is on top (or right) and which is on the bottom (or left).'),
    ('Step 3', 'Set up the double integral with appropriate limits.'),
    ('Step 4', 'Evaluate the inner integral first, then the outer integral.'),
]
for s, t in area_steps:
    story.append(Paragraph(f'<b>{s}:</b>  {t}', step_style))

story.append(Spacer(1, 0.3*cm))
story.append(img(d_area, width=10*cm))
story.append(Paragraph(
    '<i>Figure 4.4 — Shaded region enclosed between y = 2x² (parabola) and y² = 4x. '
    'Area = ∫₀¹ ∫_{2x²}^{2√x} dy dx = 2/3.</i>',
    ParagraphStyle('Caption', parent=styles['Normal'], fontSize=9,
                   alignment=TA_CENTER, textColor=colors.grey)))

story.append(Spacer(1, 0.3*cm))
story.append(Paragraph('Solved Examples', section_style))
story.append(section_line())

aex1 = [
    example_block('Find the area enclosed by y = 2x² and y² = 4x.'),
    Paragraph('<b>Solution:</b>', subsection_style),
    bullet('Intersection: Substitute y = 2x² into y² = 4x → 4x⁴ = 4x → x = 0 or x = 1'),
    bullet('At x = 1: y = 2. Points: (0,0) and (1,2)'),
    bullet('Upper curve: y = 2√x (from y² = 4x). Lower curve: y = 2x²'),
    formula('Area = ∫₀¹ ∫_{2x²}^{2√x} dy dx  =  ∫₀¹ (2√x − 2x²) dx'),
    formula('=  [4x^(3/2)/3 − 2x³/3]₀¹  =  4/3 − 2/3  =  2/3'),
    Paragraph('<b>Answer: 2/3 square units</b>', ParagraphStyle('Ans', parent=styles['Normal'],
        fontSize=11, fontName='Helvetica-Bold', textColor=colors.HexColor('#1b5e20'))),
]
for el in aex1: story.append(el)

story.append(Spacer(1, 0.2*cm))

aex2 = [
    example_block('Find the area between parabolas y² = 4ax and x² = 4ay.'),
    Paragraph('<b>Solution:</b>', subsection_style),
    bullet('Intersection: Solve simultaneously → x = 0 and x = 4a. Points (0,0) and (4a, 4a).'),
    bullet('Upper curve: y = 2√(ax). Lower curve: y = x²/(4a).'),
    formula('Area = ∫₀^{4a} ∫_{x²/(4a)}^{2√(ax)} dy dx  =  ∫₀^{4a} [2√(ax) − x²/(4a)] dx'),
    formula('=  [4√a·x^(3/2)/3 − x³/(12a)]₀^{4a}  =  32a²/3 − 16a²/3  =  16a²/3'),
    Paragraph('<b>Answer: 16a²/3 square units</b>', ParagraphStyle('Ans', parent=styles['Normal'],
        fontSize=11, fontName='Helvetica-Bold', textColor=colors.HexColor('#1b5e20'))),
]
for el in aex2: story.append(el)

story.append(Spacer(1, 0.2*cm))

aex3 = [
    example_block('Find the area of the ellipse x²/a² + y²/b² = 1.'),
    Paragraph('<b>Solution:</b>', subsection_style),
    bullet('By symmetry, Area = 4 × (area in first quadrant)'),
    bullet('In first quadrant: x: 0 → a,  y: 0 → (b/a)√(a²−x²)'),
    formula('Area = 4·(a/b)·[b²/2·sin⁻¹(x/a) + (x/2)√(a²−x²)]₀ᵃ'),
    formula('=  4·(b/a)·(b/2·π/2)·a/b  =  πab'),
    Paragraph('<b>Answer: πab square units</b>', ParagraphStyle('Ans', parent=styles['Normal'],
        fontSize=11, fontName='Helvetica-Bold', textColor=colors.HexColor('#1b5e20'))),
]
for el in aex3: story.append(el)

story.append(PageBreak())

# ════════════════════════════════════════════════
#   4.6  AREA – POLAR
# ════════════════════════════════════════════════

story.append(Paragraph('4.6  Area Enclosed by Plane Curves (Polar)', unit_style))
story.append(Spacer(1, 0.2*cm))

story.append(Paragraph('Polar Area Formula', section_style))
story.append(section_line())

story.append(Paragraph(
    'When the boundary of a region is given in polar form r = f(θ), '
    'the area is calculated using the polar double integral:', body_style))

story.append(formula('Area  =  ∬ r dr dθ  =  ∫_{θ₁}^{θ₂} ∫_{r₁(θ)}^{r₂(θ)} r dr dθ'))

story.append(Paragraph(
    'The <b>r dr dθ</b> element represents a small polar area element — '
    'think of it as a small "sector" of angular width dθ and radial width dr.', body_style))

story.append(Spacer(1, 0.2*cm))
story.append(img(d_card, width=10*cm))
story.append(Paragraph(
    '<i>Figure 4.5 — Two cardioids: r = a(1+cosθ) (blue) and r = a(1−cosθ) (red). '
    'Both have area = (3/2)πa² square units.</i>',
    ParagraphStyle('Caption', parent=styles['Normal'], fontSize=9,
                   alignment=TA_CENTER, textColor=colors.grey)))

story.append(Spacer(1, 0.3*cm))
story.append(Paragraph('Common Polar Curves and Their Areas', section_style))
story.append(section_line())

polar_curves = [
    ['Curve', 'Equation', 'Area'],
    ['Cardioid (right)', 'r = a(1 + cosθ)', '(3/2) πa²'],
    ['Cardioid (left)', 'r = a(1 − cosθ)', '(3/2) πa²'],
    ['Circle (polar)', 'r = 2a cosθ', 'πa²'],
    ['Lemniscate', 'r² = a² cos2θ', 'a²'],
]
t = Table(polar_curves, colWidths=[4*cm, 6*cm, 5*cm])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a237e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#e8eaf6'), colors.HexColor('#f5f5ff')]),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9fa8da')),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
]))
story.append(t)

story.append(Spacer(1, 0.3*cm))
story.append(Paragraph('Solved Examples', section_style))
story.append(section_line())

parea1 = [
    example_block('Find the area of the cardioid r = a(1 + cosθ).'),
    Paragraph('<b>Solution:</b>', subsection_style),
    bullet('The curve is symmetric about the initial line (θ = 0).'),
    bullet('Use symmetry: Area = 2 × (area for 0 ≤ θ ≤ π)'),
    bullet('r varies from 0 to a(1 + cosθ), θ varies from 0 to π'),
    formula('Area = 2∫₀^π ∫₀^{a(1+cosθ)} r dr dθ  =  ∫₀^π a²(1+cosθ)² dθ'),
    formula('=  a² ∫₀^π [1 + cos²θ + 2cosθ] dθ  =  (a²/2)∫₀^π [3 + cos2θ + 4cosθ] dθ'),
    formula('=  (a²/2)[3θ + sin2θ/2 + 4sinθ]₀^π  =  (a²/2)(3π)  =  3πa²/2'),
    Paragraph('<b>Answer: 3πa²/2 square units</b>', ParagraphStyle('Ans', parent=styles['Normal'],
        fontSize=11, fontName='Helvetica-Bold', textColor=colors.HexColor('#1b5e20'))),
]
for el in parea1: story.append(el)

story.append(Spacer(1, 0.2*cm))

parea2 = [
    example_block('Find the area of the lemniscate r² = a² cos2θ.'),
    Paragraph('<b>Solution:</b>', subsection_style),
    bullet('The lemniscate has two loops, each symmetric about the x-axis.'),
    bullet('Area = 4 × (area of upper half of one loop)'),
    bullet('For one loop: θ: 0 → π/4, r: 0 → a√(cos2θ)'),
    formula('Area = 4∫₀^{π/4} ∫₀^{a√cos2θ} r dr dθ  =  2∫₀^{π/4} a² cos2θ dθ'),
    formula('=  2a² [sin2θ/2]₀^{π/4}  =  2a² · (1/2)  =  a²'),
    Paragraph('<b>Answer: a² square units</b>', ParagraphStyle('Ans', parent=styles['Normal'],
        fontSize=11, fontName='Helvetica-Bold', textColor=colors.HexColor('#1b5e20'))),
]
for el in parea2: story.append(el)

story.append(PageBreak())

# ════════════════════════════════════════════════
#   4.7  TRIPLE INTEGRALS
# ════════════════════════════════════════════════

story.append(Paragraph('4.7  Triple Integrals', unit_style))
story.append(Spacer(1, 0.2*cm))

story.append(Paragraph('Definition', section_style))
story.append(section_line())

story.append(Paragraph(
    'A <b>Triple Integral</b> is an extension of the double integral to '
    'three dimensions. It is used to integrate a function f(x, y, z) over '
    'a three-dimensional region V. Physically, it computes <b>volume, mass, '
    'moment of inertia</b>, and other quantities of a 3D solid body.', body_style))

story.append(formula('∭_V f(x, y, z) dV  =  ∫∫∫ f(x, y, z) dz dy dx'))

story.append(Spacer(1, 0.2*cm))
story.append(img(d_tri, width=9*cm))
story.append(Paragraph(
    '<i>Figure 4.6 — First octant of sphere x²+y²+z²=a². '
    'The triple integral over this region gives its volume as (1/8)·(4πa³/3).</i>',
    ParagraphStyle('Caption', parent=styles['Normal'], fontSize=9,
                   alignment=TA_CENTER, textColor=colors.grey)))

story.append(Spacer(1, 0.3*cm))
story.append(Paragraph('How to Evaluate a Triple Integral', section_style))
story.append(section_line())

tri_steps = [
    ('Step 1', 'Determine the limits for z (innermost), then y, then x (outermost).'),
    ('Step 2', 'Integrate with respect to z first (treating x and y as constants). Substitute z-limits.'),
    ('Step 3', 'Integrate the result with respect to y (treating x as constant). Substitute y-limits.'),
    ('Step 4', 'Integrate the result with respect to x. Substitute x-limits to get the final answer.'),
]
for s, t in tri_steps:
    story.append(Paragraph(f'<b>{s}:</b>  {t}', step_style))

story.append(Spacer(1, 0.3*cm))
story.append(Paragraph('Solved Examples', section_style))
story.append(section_line())

tex1 = [
    example_block('Evaluate ∫₀ᵃ ∫₀ᵇ ∫₀ᶜ (x+y+z) dz dy dx'),
    Paragraph('<b>Solution:</b>', subsection_style),
    formula('Inner (dz): ∫₀ᶜ (x+y+z) dz  =  [xz+yz+z²/2]₀ᶜ  =  xc+yc+c²/2'),
    formula('Middle (dy): ∫₀ᵇ (xc+yc+c²/2) dy  =  [xcy+cy²/2+c²y/2]₀ᵇ  =  xbc+b²c/2+bc²/2'),
    formula('Outer (dx): ∫₀ᵃ (xbc+b²c/2+bc²/2) dx  =  [a²bc/2+ab²c/2+abc²/2]'),
    formula('=  abc(a+b+c)/2'),
    Paragraph('<b>Answer: abc(a+b+c)/2</b>', ParagraphStyle('Ans', parent=styles['Normal'],
        fontSize=11, fontName='Helvetica-Bold', textColor=colors.HexColor('#1b5e20'))),
]
for el in tex1: story.append(el)

story.append(Spacer(1, 0.2*cm))

tex2 = [
    example_block('Find ∭ xyz dz dy dx over the positive octant of x²+y²+z²=a².'),
    Paragraph('<b>Solution:</b>', subsection_style),
    bullet('Limits: z: 0 → √(a²−x²−y²),  y: 0 → √(a²−x²),  x: 0 → a'),
    formula('After integrating w.r.t. z then y then x:  Answer = a⁶/48'),
    Paragraph('<b>Answer: a⁶/48</b>', ParagraphStyle('Ans', parent=styles['Normal'],
        fontSize=11, fontName='Helvetica-Bold', textColor=colors.HexColor('#1b5e20'))),
]
for el in tex2: story.append(el)

story.append(PageBreak())

# ════════════════════════════════════════════════
#   4.8  VOLUME
# ════════════════════════════════════════════════

story.append(Paragraph('4.8  Volume of Solids Using Triple Integrals', unit_style))
story.append(Spacer(1, 0.2*cm))

story.append(Paragraph('Concept', section_style))
story.append(section_line())

story.append(Paragraph(
    'Just as area is computed by integrating 1 over a 2D region, '
    '<b>volume</b> is computed by integrating 1 over a 3D region. '
    'The triple integral of f(x,y,z) = 1 over a volume V gives the '
    'volume of that solid body.', body_style))

story.append(formula('Volume  =  ∭_V dV  =  ∭_V dz dy dx'))

story.append(Spacer(1, 0.2*cm))
story.append(Paragraph('Standard Volume Results', section_style))
story.append(section_line())

vol_results = [
    ['Solid', 'Volume Formula', 'Result'],
    ['Sphere x²+y²+z²=a²', '8 × first-octant integral', '4πa³/3'],
    ['Ellipsoid x²/a²+y²/b²+z²/c²=1', 'Similar to sphere', '4πabc/3'],
    ['Tetrahedron (x/a+y/b+z/c=1)', '∫∫∫ dz dy dx', 'abc/6'],
]
t = Table(vol_results, colWidths=[5*cm, 5.5*cm, 4.5*cm])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a237e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#e8eaf6'), colors.HexColor('#f5f5ff')]),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9fa8da')),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
]))
story.append(t)

story.append(Spacer(1, 0.3*cm))
story.append(Paragraph('Solved Examples', section_style))
story.append(section_line())

vex1 = [
    example_block('Find the volume of the sphere x²+y²+z²=a².'),
    Paragraph('<b>Solution:</b>', subsection_style),
    bullet('By symmetry: Volume = 8 × (first octant volume)'),
    bullet('Limits in first octant: z: 0→√(a²−x²−y²), y: 0→√(a²−x²), x: 0→a'),
    formula('V = 8∫₀ᵃ ∫₀^{√(a²-x²)} √(a²-x²-y²) dy dx'),
    formula('After integration:  V  =  4πa³/3'),
    Paragraph('<b>Answer: V = 4πa³/3 cubic units</b>', ParagraphStyle('Ans', parent=styles['Normal'],
        fontSize=11, fontName='Helvetica-Bold', textColor=colors.HexColor('#1b5e20'))),
]
for el in vex1: story.append(el)

story.append(Spacer(1, 0.2*cm))

vex2 = [
    example_block('Find the volume of the tetrahedron bounded by x/a + y/b + z/c = 1 and coordinate planes.'),
    Paragraph('<b>Solution:</b>', subsection_style),
    bullet('Limits: z: 0 → c(1 − x/a − y/b),  y: 0 → b(1 − x/a),  x: 0 → a'),
    formula('V = ∫₀ᵃ ∫₀^{b(1-x/a)} c(1-x/a-y/b) dy dx'),
    formula('After double integration:  V = abc/6'),
    Paragraph('<b>Answer: V = abc/6 cubic units</b>', ParagraphStyle('Ans', parent=styles['Normal'],
        fontSize=11, fontName='Helvetica-Bold', textColor=colors.HexColor('#1b5e20'))),
]
for el in vex2: story.append(el)

story.append(PageBreak())

# ════════════════════════════════════════════════
#   4.9  CHANGE OF VARIABLES
# ════════════════════════════════════════════════

story.append(Paragraph('4.9  Change of Variables in Integrals', unit_style))
story.append(Spacer(1, 0.2*cm))

story.append(Paragraph('4.9(a)  Cartesian to Polar Co-ordinates (Double Integral)', section_style))
story.append(section_line())

story.append(Paragraph(
    'When the region of integration is circular or contains terms like x²+y², '
    'converting to polar co-ordinates simplifies the integral significantly.', body_style))

story.append(Paragraph('<b>Transformation Substitutions:</b>', subsection_style))
story.append(formula('x = r cosθ,    y = r sinθ,    x² + y² = r²'))
story.append(formula('dx dy  →  r dr dθ    (Jacobian = r)'))

story.append(Spacer(1, 0.2*cm))
story.append(Paragraph('<b>Working Rule:</b>', subsection_style))

cart_polar_steps = [
    ('Step 1', 'Check the order of integration (make it correct if needed).'),
    ('Step 2', 'Write the boundary equations from the limits.'),
    ('Step 3', 'Sketch the region of integration.'),
    ('Step 4', 'Apply the substitution: x = r cosθ, y = r sinθ, x²+y² = r², dxdy = r dr dθ.'),
    ('Step 5', 'Determine new limits for r and θ from the sketch (draw radial strip inside the region).'),
    ('Step 6', 'Evaluate the transformed polar integral.'),
]
for s, t in cart_polar_steps:
    story.append(Paragraph(f'<b>{s}:</b>  {t}', step_style))

story.append(Spacer(1, 0.2*cm))
story.append(img(d_cp, width=10*cm))
story.append(Paragraph(
    '<i>Figure 4.7 — Converting the quarter-circle region (Cartesian) to polar form. '
    'r varies from 0 to a, θ varies from 0 to π/2.</i>',
    ParagraphStyle('Caption', parent=styles['Normal'], fontSize=9,
                   alignment=TA_CENTER, textColor=colors.grey)))

story.append(Spacer(1, 0.3*cm))
story.append(Paragraph('Solved Examples – Cartesian to Polar', section_style))
story.append(section_line())

cpex1 = [
    example_block('Evaluate ∫₀^∞ ∫₀^∞ e^(−x²−y²) dy dx using polar co-ordinates.'),
    Paragraph('<b>Solution:</b>', subsection_style),
    bullet('Region: first quadrant (x ≥ 0, y ≥ 0). In polar: θ: 0 → π/2, r: 0 → ∞'),
    formula('∫₀^{π/2} ∫₀^∞ e^{-r²} · r dr dθ'),
    bullet('Let t = r², dt = 2r dr → r dr = dt/2'),
    formula('= ∫₀^{π/2} dθ · ∫₀^∞ e^{-t} dt/2  =  (π/2) · (1/2)  =  π/4'),
    Paragraph('<b>Answer: π/4</b>', ParagraphStyle('Ans', parent=styles['Normal'],
        fontSize=11, fontName='Helvetica-Bold', textColor=colors.HexColor('#1b5e20'))),
    note('This result is used to prove that ∫₀^∞ e^{-x²} dx = √π/2 — a fundamental result in probability!'),
]
for el in cpex1: story.append(el)

story.append(Spacer(1, 0.2*cm))

cpex2 = [
    example_block('Evaluate ∫₀^{2a} ∫₀^{√(2ax−x²)} (x²+y²) dy dx by converting to polar.'),
    Paragraph('<b>Solution:</b>', subsection_style),
    bullet('Boundary: y = √(2ax − x²) → y² = 2ax − x² → x²+y²−2ax=0 → circle with centre (a,0) radius a.'),
    bullet('In polar: r = 2a cosθ. Limits: r: 0 → 2a cosθ,  θ: 0 → π/2'),
    formula('∫₀^{π/2} ∫₀^{2acosθ} r² · r dr dθ  =  ∫₀^{π/2} ∫₀^{2acosθ} r³ dr dθ'),
    formula('=  ∫₀^{π/2} [r⁴/4]₀^{2acosθ} dθ  =  4a⁴ ∫₀^{π/2} cos⁴θ dθ'),
    formula('=  4a⁴ · (3/4)·(1/2)·(π/2)  =  3πa⁴/4'),
    Paragraph('<b>Answer: 3πa⁴/4</b>', ParagraphStyle('Ans', parent=styles['Normal'],
        fontSize=11, fontName='Helvetica-Bold', textColor=colors.HexColor('#1b5e20'))),
]
for el in cpex2: story.append(el)

story.append(PageBreak())

# ── 4.9(b) Cylindrical ──

story.append(Paragraph('4.9(b)  Cylindrical Co-ordinates', section_style))
story.append(section_line())

story.append(Paragraph(
    'Cylindrical co-ordinates are used when the region has <b>circular cross-sections '
    'at every height z</b> — like cylinders, cones, and paraboloids. '
    'It is essentially polar co-ordinates in the x-y plane with z unchanged.', body_style))

story.append(Paragraph('<b>Transformation:</b>', subsection_style))
story.append(formula('x = r cosθ,    y = r sinθ,    z = z'))
story.append(formula('dx dy dz  →  r dr dθ dz    (Jacobian = r)'))

story.append(Spacer(1, 0.2*cm))

story.append(img(d_cyl, width=9*cm))
story.append(Paragraph(
    '<i>Figure 4.8 — Cylinder x²+y²=1, z=0 to 2 in cylindrical co-ordinates. '
    'The green base and orange top cap are clearly visible.</i>',
    ParagraphStyle('Caption', parent=styles['Normal'], fontSize=9,
                   alignment=TA_CENTER, textColor=colors.grey)))

story.append(Spacer(1, 0.2*cm))
story.append(Paragraph('<b>When to use Cylindrical Co-ordinates?</b>', subsection_style))
for txt in [
    'The region involves a <b>cylinder</b> (x²+y²=a²) or a <b>paraboloid</b> (z=x²+y²).',
    'The integrand contains the expression <b>x²+y²</b>.',
    'The cross-section parallel to the xy-plane is <b>circular</b>.',
]:
    story.append(bullet(txt))

story.append(Spacer(1, 0.2*cm))
story.append(Paragraph('Solved Example – Cylindrical Co-ordinates', section_style))
story.append(section_line())

cylex1 = [
    example_block('Find the volume of the cylinder x²+y²=1 between z=0 and z=4−r².'),
    Paragraph('<b>Solution:</b>', subsection_style),
    bullet('Convert: r² = 1, so r: 0 → 1; z: 0 → 4 − r²; θ: 0 → 2π'),
    formula('V = ∫₀^{2π} ∫₀¹ ∫₀^{4-r²} r dz dr dθ'),
    formula('= ∫₀^{2π} ∫₀¹ r(4−r²) dr dθ  =  ∫₀^{2π} [2r²−r⁴/4]₀¹ dθ'),
    formula('= ∫₀^{2π} (7/4) dθ  =  7π/2'),
    Paragraph('<b>Answer: 7π/2 cubic units</b>', ParagraphStyle('Ans', parent=styles['Normal'],
        fontSize=11, fontName='Helvetica-Bold', textColor=colors.HexColor('#1b5e20'))),
]
for el in cylex1: story.append(el)

story.append(Spacer(1, 0.3*cm))

# ── 4.9(c) Spherical ──

story.append(Paragraph('4.9(c)  Spherical Polar Co-ordinates', section_style))
story.append(section_line())

story.append(Paragraph(
    'Spherical co-ordinates are ideal when the region is <b>spherical or has '
    'spherical symmetry</b>. The point (x,y,z) is described by its distance r '
    'from the origin, polar angle θ from the z-axis, and azimuthal angle φ in '
    'the xy-plane.', body_style))

story.append(Paragraph('<b>Transformation:</b>', subsection_style))
story.append(formula('x = r sinθ cosφ,    y = r sinθ sinφ,    z = r cosθ'))
story.append(formula('dx dy dz  →  r² sinθ dr dθ dφ    (Jacobian = r² sinθ)'))

story.append(Spacer(1, 0.2*cm))
story.append(img(d_sph, width=9*cm))
story.append(Paragraph(
    '<i>Figure 4.9 — Spherical polar co-ordinates: r = distance from origin, '
    'θ = polar angle from z-axis, φ = azimuthal angle in xy-plane.</i>',
    ParagraphStyle('Caption', parent=styles['Normal'], fontSize=9,
                   alignment=TA_CENTER, textColor=colors.grey)))

story.append(Spacer(1, 0.2*cm))
story.append(Paragraph('<b>Standard Limits (Full Sphere):</b>', subsection_style))
story.append(formula('r: 0 → a,    θ: 0 → π,    φ: 0 → 2π'))

story.append(Spacer(1, 0.2*cm))
story.append(Paragraph('Solved Example – Spherical Co-ordinates', section_style))
story.append(section_line())

spex1 = [
    example_block('Evaluate ∭ 1/√(1−x²−y²−z²) dV over the sphere x²+y²+z²=1.'),
    Paragraph('<b>Solution:</b>', subsection_style),
    bullet('Convert: 1−x²−y²−z² = 1−r², dV = r² sinθ dr dθ dφ'),
    bullet('Limits: r: 0→1, θ: 0→π, φ: 0→2π'),
    formula('= ∫₀^{2π} dφ · ∫₀^π sinθ dθ · ∫₀¹ r²/√(1−r²) dr'),
    formula('= 2π × 2 × ∫₀¹ r²/√(1−r²) dr'),
    bullet('Put r = sint, dr = cost dt → ∫₀^{π/2} sin²t dt = π/4'),
    formula('= 4π × (π/4)  =  π²'),
    Paragraph('<b>Answer: π²</b>', ParagraphStyle('Ans', parent=styles['Normal'],
        fontSize=11, fontName='Helvetica-Bold', textColor=colors.HexColor('#1b5e20'))),
]
for el in spex1: story.append(el)

story.append(PageBreak())

# ════════════════════════════════════════════════
#   ADVANTAGES & DISADVANTAGES
# ════════════════════════════════════════════════

story.append(Paragraph('Advantages and Disadvantages of Key Methods', unit_style))
story.append(Spacer(1, 0.2*cm))

story.append(Paragraph('Double Integration – Cartesian Co-ordinates', section_style))
story.append(section_line())

story.append(Paragraph('<b>Advantages:</b>', subsection_style))
for txt in [
    'Simple and straightforward to apply when limits are constants or simple algebraic functions.',
    'Easy to visualize regions as rectangular or triangular shapes in the xy-plane.',
    'Direct application to problems involving rectangular domains without any substitution.',
    'Both orders dy dx and dx dy can be chosen based on which gives simpler limits.',
]:
    story.append(bullet(txt))

story.append(Paragraph('<b>Disadvantages:</b>', subsection_style))
for txt in [
    'Becomes very complicated when the region is circular or has curved boundaries — limits involve square roots.',
    'The integrand may contain x²+y² terms that do not simplify easily in Cartesian form.',
    'For problems involving circles or ellipses, the limits become functions, making evaluation tedious.',
    'Not suitable for problems that are symmetric about a point (radial symmetry), as polar form is more natural.',
]:
    story.append(bullet(txt))

story.append(Spacer(1, 0.2*cm))
story.append(Paragraph('Double Integration – Polar Co-ordinates', section_style))
story.append(section_line())

story.append(Paragraph('<b>Advantages:</b>', subsection_style))
for txt in [
    'Extremely convenient for circular, annular, or radially symmetric regions — limits become simple constants.',
    'Integrand containing x²+y² simplifies immediately to r².',
    'Area of cardioids, lemniscates, and other polar curves is easily computed.',
    'Used in evaluating important integrals like ∫₀^∞ e^{-x²} dx = √π/2.',
]:
    story.append(bullet(txt))

story.append(Paragraph('<b>Disadvantages:</b>', subsection_style))
for txt in [
    'Requires familiarity with polar curve sketching — a common source of errors.',
    'The Jacobian factor "r" must always be included; forgetting it is a frequent mistake.',
    'Limits can become non-trivial when the region is not purely radially symmetric.',
    'Not suitable for regions with straight-line boundaries (triangles, squares), where Cartesian is simpler.',
]:
    story.append(bullet(txt))

story.append(Spacer(1, 0.2*cm))
story.append(Paragraph('Change of Order of Integration', section_style))
story.append(section_line())

story.append(Paragraph('<b>Advantages:</b>', subsection_style))
for txt in [
    'Converts a difficult or impossible integral into an easily evaluable one.',
    'Allows us to evaluate integrals where the inner integral has no closed form (e.g., sin(x)/x).',
    'Helps evaluate double integrals over complex regions by splitting into simpler sub-regions.',
    'Important technique for MSBTE examinations — saves time when the original order is difficult.',
]:
    story.append(bullet(txt))

story.append(Paragraph('<b>Disadvantages:</b>', subsection_style))
for txt in [
    'Requires careful region sketching — an incorrect sketch leads to wrong limits.',
    'When the region splits into R₁ and R₂, both sub-regions must be handled separately, increasing work.',
    'Not always obvious whether changing the order will simplify the problem.',
]:
    story.append(bullet(txt))

story.append(Spacer(1, 0.2*cm))
story.append(Paragraph('Triple Integrals / Change of Variables', section_style))
story.append(section_line())

story.append(Paragraph('<b>Advantages:</b>', subsection_style))
for txt in [
    'Triple integrals directly give volume, mass, moment, and centre of gravity of 3D solids.',
    'Cylindrical co-ordinates make cylinder and cone problems extremely simple to set up.',
    'Spherical co-ordinates reduce sphere problems to integrating simple trigonometric functions.',
    'The Jacobian transformation is a systematic and reliable way to change variables in any dimension.',
]:
    story.append(bullet(txt))

story.append(Paragraph('<b>Disadvantages:</b>', subsection_style))
for txt in [
    'The Jacobian (r for cylindrical, r² sinθ for spherical) must be included — easy to forget.',
    'Visualizing 3D regions requires spatial thinking, which is more challenging than 2D regions.',
    'Setting up correct limits in 3D (especially for odd shapes) requires careful analysis.',
    'Triple integrals with variable limits involve much more algebraic computation than double integrals.',
]:
    story.append(bullet(txt))

story.append(PageBreak())

# ════════════════════════════════════════════════
#   QUICK REFERENCE / FORMULA SHEET
# ════════════════════════════════════════════════

story.append(Paragraph('Quick Reference Formula Sheet', unit_style))
story.append(Spacer(1, 0.2*cm))

story.append(Paragraph('All Key Formulas at a Glance', section_style))
story.append(section_line())

ref_data = [
    ['Topic', 'Formula / Key Result'],
    ['Double Integral (Cartesian)', '∫_a^b ∫_{f₁}^{f₂} f(x,y) dy dx'],
    ['Separable Integral', '∫_a^b∫_c^d f(x)g(y) dy dx = [∫f dx][∫g dy]'],
    ['Polar Double Integral', '∫∫ f(r,θ) r dr dθ   (note: Jacobian = r)'],
    ['Cartesian → Polar', 'x=r cosθ, y=r sinθ, dx dy = r dr dθ'],
    ['Area (Cartesian)', '∬_R dA = ∫∫ dy dx'],
    ['Area (Polar)', '∬ r dr dθ'],
    ['Area of Ellipse', 'πab'],
    ['Area of Cardioid r=a(1±cosθ)', '3πa²/2'],
    ['Area of Circle r=2a cosθ', 'πa²'],
    ['Area of Lemniscate r²=a²cos2θ', 'a²'],
    ['Triple Integral', '∭_V f dV = ∫∫∫ f dz dy dx'],
    ['Volume of Sphere', '4πa³/3'],
    ['Volume of Ellipsoid', '4πabc/3'],
    ['Volume of Tetrahedron', 'abc/6'],
    ['Cylindrical Jacobian', 'J = r   (dx dy dz = r dr dθ dz)'],
    ['Cylindrical Transform', 'x=r cosθ, y=r sinθ, z=z'],
    ['Spherical Jacobian', 'J = r² sinθ   (dx dy dz = r² sinθ dr dθ dφ)'],
    ['Spherical Transform', 'x=r sinθ cosφ, y=r sinθ sinφ, z=r cosθ'],
    ['Walli\'s: ∫₀^{π/2} sinⁿ or cosⁿ (n even)', '[(n-1)/n · (n-3)/(n-2) · ... · 1/2] · π/2'],
    ['Walli\'s: ∫₀^{π/2} sinⁿ or cosⁿ (n odd)', '[(n-1)/n · (n-3)/(n-2) · ... · 2/3]'],
    ['Famous Result', '∫₀^∞ ∫₀^∞ e^{-(x²+y²)} dy dx = π/4'],
]

t = Table(ref_data, colWidths=[6*cm, 9*cm])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a237e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9.5),
    ('ALIGN', (0,0), (0,-1), 'LEFT'),
    ('ALIGN', (1,0), (1,-1), 'LEFT'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#e8eaf6'), colors.HexColor('#f5f5ff')]),
    ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9fa8da')),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
]))
story.append(t)

story.append(Spacer(1, 0.4*cm))
story.append(Paragraph('Important Notes for MSBTE Examinations', section_style))
story.append(section_line())

exam_notes = [
    'Always <b>check the correct form</b> of the integral before evaluating — inner limits must match the inner variable.',
    'For <b>polar integrals</b>, never forget the extra factor <b>"r"</b> (Jacobian). This is the most common error.',
    'For <b>Change of Order</b>, always draw the region diagram first. The limits follow directly from the diagram.',
    'When using <b>symmetry</b> (e.g., for cardioids), multiply the half-region result by 2 or 4 as appropriate.',
    'The <b>Walli\'s formula</b> is essential for evaluating trigonometric integrals in polar and spherical problems.',
    'For <b>triple integrals</b>, set up limits from innermost (z) to outermost (x) — z first, y second, x last.',
    'Volume of sphere = <b>4πa³/3</b>, volume of ellipsoid = <b>4πabc/3</b> — memorise these!',
    'The <b>Jacobian</b> for cylindrical = r; for spherical = r² sinθ. These must be included as extra factors.',
]
for i, note_text in enumerate(exam_notes, 1):
    story.append(Paragraph(f'<b>{i}.</b>  {note_text}', step_style))

story.append(Spacer(1, 0.4*cm))

# Final banner
final_data = [['Best of Luck in Your MSBTE K-Scheme Examinations! 🎯']]
ft = Table(final_data, colWidths=[PAGE_W - 2*MARGIN])
ft.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#1a237e')),
    ('TEXTCOLOR', (0,0), (-1,-1), colors.white),
    ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 14),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('TOPPADDING', (0,0), (-1,-1), 12),
    ('BOTTOMPADDING', (0,0), (-1,-1), 12),
]))
story.append(ft)

# ─────────────────── BUILD PDF ───────────────────

def add_header_footer(canvas, doc):
    canvas.saveState()
    page_num = canvas.getPageNumber()
    # Header
    if page_num > 1:
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(colors.HexColor('#37474f'))
        canvas.drawString(MARGIN, PAGE_H - 1.2*cm,
                          'MSBTE K-Scheme | Engineering Mathematics II | Unit IV – Multiple Integrals')
        canvas.setStrokeColor(colors.HexColor('#90caf9'))
        canvas.line(MARGIN, PAGE_H - 1.35*cm, PAGE_W - MARGIN, PAGE_H - 1.35*cm)
    # Footer
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(colors.HexColor('#37474f'))
    canvas.drawCentredString(PAGE_W/2, 1.2*cm, f'Page {page_num}')
    canvas.setStrokeColor(colors.HexColor('#90caf9'))
    canvas.line(MARGIN, 1.5*cm, PAGE_W - MARGIN, 1.5*cm)
    canvas.restoreState()

print("Building PDF...")
doc.build(story, onFirstPage=add_header_footer, onLaterPages=add_header_footer)
print(f"PDF built successfully at {os.path.join(OUTPUT_DIR, 'MSBTE_Multiple_Integrals_Guide.pdf')}")