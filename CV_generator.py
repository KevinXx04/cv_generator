# -*- coding: utf-8 -*-
from fpdf import FPDF

class CV_PDF(FPDF):
    def header(self):
        # Header del documento
        pass
    
    def footer(self):
        # Footer con número de página
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

# Crear instancia del PDF
pdf = CV_PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Colores
AZUL_PRINCIPAL = (41, 128, 185)
GRIS_OSCURO = (44, 62, 80)
GRIS_CLARO = (189, 195, 199)

# ========== ENCABEZADO ==========
pdf.set_font('Arial', 'B', 24)
pdf.set_text_color(*AZUL_PRINCIPAL)
pdf.cell(0, 12, 'Kevin Alonso Alvarado Vargas', 0, 1, 'C')
pdf.ln(2)

# Información de contacto
pdf.set_font('Arial', '', 10)
pdf.set_text_color(*GRIS_OSCURO)
pdf.cell(0, 6, 'Barranca Puntarenas, Costa Rica', 0, 1, 'C')
pdf.cell(0, 6, 'Teléfono: +506 8898 9466 | Móvil: 208670217', 0, 1, 'C')
pdf.cell(0, 6, 'Email: ualvaradokevin2005@gmail.com', 0, 1, 'C')
pdf.cell(0, 6, 'Fecha de nacimiento: 25/06/2005 | Nacionalidad: Costarricense', 0, 1, 'C')
pdf.set_font('Arial', 'I', 10)
pdf.set_text_color(*AZUL_PRINCIPAL)
pdf.cell(0, 6, 'LinkedIn: www.linkedin.com/in/kevinalvaradovargas', 0, 1, 'C')
pdf.ln(5)

# Línea separadora
pdf.set_draw_color(*AZUL_PRINCIPAL)
pdf.set_line_width(0.5)
pdf.line(10, pdf.get_y(), 200, pdf.get_y())
pdf.ln(8)

# ========== FORMACIÓN ==========
pdf.set_font('Arial', 'B', 14)
pdf.set_text_color(*AZUL_PRINCIPAL)
pdf.cell(0, 8, 'FORMACIÓN', 0, 1, 'L')
pdf.ln(2)

formacion = [
    {
        'periodo': 'Marzo 2023 - Abril 2027',
        'institucion': 'Universidad de Costa Rica Sede del Pacífico',
        'titulo': 'Bachillerato en Informática Empresarial',
        'estado': 'Estudiante activo'
    },
    {
        'periodo': 'Noviembre 2025 - Diciembre 2025',
        'institucion': 'Skilio - Andorra la Vella, Andorra',
        'titulo': 'Certificado de uso de inteligencia artificial',
        'estado': 'Informática'
    },
    {
        'periodo': 'Octubre 2025 - Diciembre 2025',
        'institucion': 'Skilio - Andorra la Vella, Andorra',
        'titulo': 'Curso completo para aprender inglés desde cero',
        'estado': 'Idiomas'
    },
    {
        'periodo': 'Septiembre 2025 - Diciembre 2025',
        'institucion': 'Skilio - Andorra la Vella, Andorra',
        'titulo': 'Curso completo de automatizaciones con Make',
        'estado': 'Informática'
    },
    {
        'periodo': 'Octubre 2025 - Diciembre 2025',
        'institucion': 'Skilio - Andorra la Vella, Andorra',
        'titulo': 'Curso N8N: aprende a crear y vender agentes de IA',
        'estado': 'Informática'
    },
    {
        'periodo': 'Septiembre 2025 - Diciembre 2025',
        'institucion': 'Skilio - Andorra la Vella, Andorra',
        'titulo': 'Curso de inteligencia artificial desde cero',
        'estado': 'Informática'
    }
]

for item in formacion:
    pdf.set_font('Arial', 'B', 10)
    pdf.set_text_color(*GRIS_OSCURO)
    pdf.cell(0, 6, item['periodo'], 0, 1, 'L')
    
    pdf.set_font('Arial', 'B', 11)
    pdf.set_text_color(*AZUL_PRINCIPAL)
    pdf.cell(0, 6, item['institucion'], 0, 1, 'L')
    
    pdf.set_font('Arial', '', 10)
    pdf.set_text_color(*GRIS_OSCURO)
    pdf.cell(0, 5, f"{item['titulo']} - {item['estado']}", 0, 1, 'L')
    pdf.ln(2)

pdf.ln(3)

# ========== HISTORIAL LABORAL ==========
pdf.set_font('Arial', 'B', 14)
pdf.set_text_color(*AZUL_PRINCIPAL)
pdf.cell(0, 8, 'HISTORIAL LABORAL', 0, 1, 'L')
pdf.ln(2)

pdf.set_font('Arial', 'B', 10)
pdf.set_text_color(*GRIS_OSCURO)
pdf.cell(0, 6, 'Agosto 2025 - Diciembre 2025', 0, 1, 'L')

pdf.set_font('Arial', 'B', 11)
pdf.set_text_color(*AZUL_PRINCIPAL)
pdf.cell(0, 6, 'FUNCAVIDA - Alajuela, San Ramón', 0, 1, 'L')

pdf.set_font('Arial', 'I', 10)
pdf.set_text_color(*GRIS_OSCURO)
pdf.cell(0, 5, 'Ingeniero de Software Freelance', 0, 1, 'L')
pdf.ln(1)

pdf.set_font('Arial', '', 9)
pdf.multi_cell(0, 5, 'Mi contribución abarcó todas las etapas clave del proyecto, incluyendo la implementación de la metodología Scrum, el diseño y gestión de la base de datos, el desarrollo de la API, las tareas de aseguramiento de calidad (QA), así como el diseño, el back-end y el front-end. Esto me permitió garantizar el correcto funcionamiento del sistema destinado a apoyar la organización de supervivientes de cáncer.')
pdf.ln(5)

# ========== COMPETENCIAS ==========
pdf.set_font('Arial', 'B', 14)
pdf.set_text_color(*AZUL_PRINCIPAL)
pdf.cell(0, 8, 'COMPETENCIAS', 0, 1, 'L')
pdf.ln(2)

# Competencias técnicas
competencias_tecnicas = [
    'Java', 'C#', 'PHP', 'Python', 'JavaScript', 'Git', 'GitHub',
    'Word', 'Excel', 'PowerPoint', 'HTML', 'CSS', 'Bootstrap',
    'Docker', 'Bases de datos relacionales', 'APIs', 'Bash', 'Linux', 'Windows'
]

pdf.set_font('Arial', 'B', 11)
pdf.set_text_color(*GRIS_OSCURO)
pdf.cell(0, 6, 'Competencias Técnicas:', 0, 1, 'L')
pdf.set_font('Arial', '', 9)

# Crear lista de competencias en columnas
x_start = pdf.get_x()
y_start = pdf.get_y()
col_width = 60
row_height = 5
col = 0

for i, comp in enumerate(competencias_tecnicas):
    if col == 3:
        col = 0
        pdf.ln(row_height)
    
    pdf.set_x(10 + col * col_width)
    pdf.cell(col_width, row_height, f'- {comp}', 0, 0, 'L')
    col += 1

pdf.ln(row_height + 3)

# Competencias profesionales
competencias_profesionales = [
    'Diagnóstico de fallos', 'Diseño API', 'Desarrollo de software',
    'Precisión y eficacia', 'Gestión de proyectos', 'Trabajo en equipo',
    'Adaptabilidad', 'Autodidactismo', 'Facilidad para trabajar bajo presión',
    'Empatía'
]

pdf.set_font('Arial', 'B', 11)
pdf.set_text_color(*GRIS_OSCURO)
pdf.cell(0, 6, 'Competencias Profesionales:', 0, 1, 'L')
pdf.set_font('Arial', '', 9)

col = 0
for i, comp in enumerate(competencias_profesionales):
    if col == 3:
        col = 0
        pdf.ln(row_height)
    
    pdf.set_x(10 + col * col_width)
    pdf.cell(col_width, row_height, f'- {comp}', 0, 0, 'L')
    col += 1

pdf.ln(row_height + 5)

# ========== IDIOMAS ==========
pdf.set_font('Arial', 'B', 14)
pdf.set_text_color(*AZUL_PRINCIPAL)
pdf.cell(0, 8, 'IDIOMAS', 0, 1, 'L')
pdf.ln(2)

idiomas = [
    {'idioma': 'Español', 'nivel': 'C2 - Experto'},
    {'idioma': 'Inglés', 'nivel': 'C1 - Avanzado'},
    {'idioma': 'Portugués', 'nivel': 'A2 - Básico'}
]

pdf.set_font('Arial', '', 10)
pdf.set_text_color(*GRIS_OSCURO)
for lang in idiomas:
    pdf.cell(50, 6, f'- {lang["idioma"]}:', 0, 0, 'L')
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 6, lang['nivel'], 0, 1, 'L')
    pdf.set_font('Arial', '', 10)

pdf.ln(5)

# ========== CERTIFICACIONES ==========
pdf.set_font('Arial', 'B', 14)
pdf.set_text_color(*AZUL_PRINCIPAL)
pdf.cell(0, 8, 'CERTIFICACIONES', 0, 1, 'L')
pdf.ln(2)

pdf.set_font('Arial', '', 9)
pdf.set_text_color(*GRIS_OSCURO)
pdf.cell(0, 5, 'Carpeta con todas mis certificaciones:', 0, 1, 'L')
pdf.set_font('Arial', '', 8)
pdf.set_text_color(*AZUL_PRINCIPAL)
pdf.cell(0, 5, 'drive.google.com/drive/folders/1wXMZeubfi6Gx4201_uv_xyJO2ZsBz2xq', 0, 1, 'L')

# Guardar el PDF
try:
    output_path = r'C:\Users\User\Downloads\KevinAlonso_AlvaradoVargas_CV.pdf'
    pdf.output(output_path)
    print(f'CV generado exitosamente en: {output_path}')
except Exception as e:
    print(f'Error al generar el PDF: {e}')
    import traceback
    traceback.print_exc()
