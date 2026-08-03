// Skills and technologies data
export const skillsData = {
  // Section configuration
  sectionId: "skills",
  title: "Competencias y Habilidades",
  subtitle: "Experiencia profesional en recursos humanos, procesos organizacionales y herramientas especializadas",
  
  // Layout configuration
  layout: {
    wrapperClass: "wrapper style3",
    containerClass: "container",
    gridClass: "row gtr-uniform"
  },
  
  // Skills with proficiency levels (matching profile percentages)
  skillsets: [
    {
      name: "Reclutamiento y Selección",
      level: 95,
      description: "Experiencia avanzada en procesos completos de reclutamiento y selección de personal",
      yearsExperience: "2+ años",
      proficiencyLevel: "Avanzado",
      icon: "fas fa-users",
      techColor: "#3776ab",
      hoverDescription: "Gestión completa de procesos de reclutamiento desde levantamiento de perfil hasta feedback final, optimizando etapas y garantizando experiencia positiva",
      tags: [
        "Herramientas de Selección",
        "Herramientas de Sourcing",
        "LinkedIn Recruiter",
        "SuccessFactors",
        "Evaluación de Candidatos",
        "Entrevistas Estructuradas"
      ]
    },
    {
      name: "Gestión de Procesos",
      level: 90,
      description: "Especialización en optimización y gestión de procesos organizacionales",
      yearsExperience: "4+ años",
      proficiencyLevel: "Avanzado",
      icon: "fas fa-cogs",
      techColor: "#ff6b6b",
      hoverDescription: "Experiencia en gestión de procesos comerciales, mejora continua, coordinación de tareas simultáneas y optimización de workflows",
      tags: [
        "Mejora Continua",
        "Optimización de Procesos",
        "Gestión Simultánea",
        "Control de Calidad",
        "Protocolos de Calidad",
        "Gestión Logística",
        "Análisis de Procesos",
        "Eficiencia Operacional"
      ]
    },
    {
      name: "Atención al Cliente",
      level: 85,
      description: "Experiencia sólida en atención al cliente y experiencia del usuario",
      yearsExperience: "4+ años",
      proficiencyLevel: "Avanzado",
      icon: "fas fa-handshake",
      techColor: "#4dabf7",
      hoverDescription: "Gestión integral de atención al cliente, ventas, postventa y mejora de la experiencia del usuario en procesos comerciales",
      tags: [
        "Experiencia del Cliente",
        "Atención Postventa",
        "Gestión de Ventas",
        "Resolución de Conflictos",
        "Comunicación Efectiva",
        "Satisfacción del Cliente",
        "Procesos Comerciales",
        "Calidad de Servicio"
      ]
    },
    {
      name: "Herramientas Especializadas",
      level: 80,
      description: "Manejo intermedio de herramientas de recursos humanos y sistemas empresariales",
      yearsExperience: "2+ años",
      proficiencyLevel: "Intermedio",
      icon: "fas fa-tools",
      techColor: "#28a745",
      hoverDescription: "Experiencia práctica con herramientas especializadas en reclutamiento, sistemas de gestión empresarial y análisis de datos",
      tags: [
        "Excel Intermedio",
        "LinkedIn Recruiter Básico",
        "SuccessFactors Básico",
        "SAP Básico",
        "Herramientas de Sourcing",
        "Sistemas de Gestión",
        "Análisis de Datos",
        "Reportes"
      ]
    },
    {
      name: "Habilidades Blandas",
      level: 95,
      description: "Competencias interpersonales y de liderazgo desarrolladas a través de la experiencia profesional",
      yearsExperience: "4+ años",
      proficiencyLevel: "Avanzado",
      icon: "fas fa-heart",
      techColor: "#fd7e14",
      hoverDescription: "Habilidades sólidas en trabajo en equipo, comunicación efectiva, proactividad, resiliencia y adaptación al cambio",
      tags: [
        "Proactividad",
        "Resiliencia",
        "Colaboración",
        "Comunicación Efectiva",
        "Trabajo en Equipo",
        "Adaptación",
        "Orientación a Resultados",
        "Orientación al Detalle"
      ]
    },
    {
      name: "Gestión de SLA y Deadlines",
      level: 90,
      description: "Experiencia en cumplimiento de acuerdos de nivel de servicio y gestión de plazos",
      yearsExperience: "3+ años",
      proficiencyLevel: "Avanzado",
      icon: "fas fa-clock",
      techColor: "#6c757d",
      hoverDescription: "Especialización en gestión de SLA, cumplimiento de deadlines, planificación estratégica y seguimiento de indicadores de desempeño",
      tags: [
        "Gestión de SLA",
        "Cumplimiento de Deadlines",
        "Planificación Estratégica",
        "KPIs",
        "Seguimiento de Procesos",
        "Gestión del Tiempo",
        "Priorization",
        "Eficiencia"
      ]
    }
  ],
  
  // Additional skills categorization for AboutUnified component
  categories: [
    {
      name: "Reclutamiento y Selección",
      skills: [
        {
          name: "Herramientas de Selección",
          icon: "fas fa-users",
          proficiency: "Intermedio",
          yearsExperience: "2+ años",
          description: "Uso de herramientas especializadas para procesos de selección de personal",
          specialties: ["Evaluación de Candidatos", "Filtros de Selección", "Entrevistas Estructuradas", "Assessment"]
        },
        {
          name: "Herramientas de Sourcing",
          icon: "fas fa-search",
          proficiency: "Intermedio",
          yearsExperience: "2+ años",
          description: "Identificación y atracción de talento usando múltiples canales",
          specialties: ["Búsqueda Activa", "Búsqueda Pasiva", "Redes Profesionales", "Headhunting"]
        },
        {
          name: "LinkedIn Recruiter",
          icon: "fab fa-linkedin",
          proficiency: "Básico",
          yearsExperience: "1+ año",
          description: "Uso de LinkedIn Recruiter para sourcing y reclutamiento",
          specialties: ["Sourcing Digital", "Networking Profesional", "Talent Pipeline", "InMail"]
        }
      ]
    },
    {
      name: "Gestión de Procesos",
      skills: [
        {
          name: "Análisis de Procesos",
          icon: "fas fa-chart-line",
          proficiency: "Avanzado",
          yearsExperience: "3+ años",
          description: "Análisis y optimización de procesos organizacionales",
          specialties: ["Mejora Continua", "Eficiencia Operacional", "Mapeo de Procesos", "KPIs"]
        },
        {
          name: "Control de Calidad",
          icon: "fas fa-check-circle",
          proficiency: "Avanzado",
          yearsExperience: "2+ años",
          description: "Implementación y seguimiento de protocolos de calidad",
          specialties: ["Protocolos de Calidad", "Auditorías", "Cumplimiento", "Documentación"]
        },
        {
          name: "Gestión de SLA",
          icon: "fas fa-clock",
          proficiency: "Avanzado",
          yearsExperience: "3+ años",
          description: "Gestión de acuerdos de nivel de servicio y deadlines",
          specialties: ["Cumplimiento de Deadlines", "Indicadores de Desempeño", "Seguimiento", "Planificación"]
        }
      ]
    },
    {
      name: "Herramientas Empresariales",
      skills: [
        {
          name: "Excel",
          icon: "fas fa-file-excel",
          proficiency: "Intermedio",
          yearsExperience: "3+ años",
          description: "Análisis de datos y reportes usando Excel avanzado",
          specialties: ["Fórmulas Avanzadas", "Tablas Dinámicas", "Gráficos", "Automatización"]
        },
        {
          name: "SuccessFactors",
          icon: "fas fa-users-cog",
          proficiency: "Básico",
          yearsExperience: "1+ año",
          description: "Sistema de gestión de recursos humanos de SAP",
          specialties: ["Gestión de Talento", "Evaluaciones", "Onboarding", "Reportes HR"]
        },
        {
          name: "SAP",
          icon: "fas fa-database",
          proficiency: "Básico",
          yearsExperience: "1+ año",
          description: "Sistema empresarial para gestión de recursos",
          specialties: ["Módulos HR", "Consultas Básicas", "Reportes", "Navegación"]
        }
      ]
    },
    {
      name: "Habilidades Interpersonales",
      skills: [
        {
          name: "Comunicación Efectiva",
          icon: "fas fa-comments",
          proficiency: "Avanzado",
          yearsExperience: "4+ años",
          description: "Comunicación clara y asertiva con diferentes audiencias",
          specialties: ["Presentaciones", "Entrevistas", "Negociación", "Feedback"]
        },
        {
          name: "Trabajo en Equipo",
          icon: "fas fa-users",
          proficiency: "Avanzado",
          yearsExperience: "4+ años",
          description: "Colaboración efectiva con equipos multidisciplinarios",
          specialties: ["Liderazgo", "Colaboración", "Resolución de Conflictos", "Adaptabilidad"]
        },
        {
          name: "Orientación a Resultados",
          icon: "fas fa-target",
          proficiency: "Avanzado",
          yearsExperience: "4+ años",
          description: "Enfoque en el logro de objetivos y metas organizacionales",
          specialties: ["Planificación Estratégica", "Seguimiento", "Proactividad", "Mejora Continua"]
        }
      ]
    }
  ],
  
  // Skill statistics
  statistics: {
    totalSkills: 15,
    expertLevel: 0,
    advancedLevel: 4,
    intermediateLevel: 2,
    certifications: 0
  }
};