// Work Experience Data
export const workData = {
  // Section configuration
  sectionId: "work",
  title: "Experiencia Profesional",
  subtitle: "Mi trayectoria profesional y logros destacados",
  
  // Layout configuration
  layout: {
    wrapperClass: "wrapper style1 fade-up",
    containerClass: "container"
  },
  
  // Work experiences (ordered by most recent first)
  experiences: [
    {
      id: "hello-there-analista-procesos",
      company: "Hello There",
      position: "Analista de Procesos, Ventas y Experiencia del Cliente",
      duration: "04/jun/2020 - 31/12/2024",
      location: "Paraguay",
      type: "Tiempo completo",
      status: "completed",
      
      description: "Gestioné procesos comerciales integrales, incluyendo compras, ventas, atención al cliente y postventa, asegurando calidad y satisfacción. Coordiné múltiples tareas simultáneamente, implementando mejoras continuas y optimizando procesos logísticos.",
      
      responsibilities: [
        "Gestión de procesos comerciales integrales incluyendo compras, ventas y atención al cliente",
        "Coordinación de múltiples tareas simultáneamente",
        "Implementación de mejoras continuas en procesos",
        "Optimización de procesos logísticos y tiempos de entrega",
        "Resolución de incidencias y atención postventa"
      ],
      
      technologies: [
        "Gestión de Procesos", "Atención al Cliente", "Ventas", 
        "Logística", "Mejora Continua", "Experiencia del Cliente"
      ],
      
      achievements: [
        "Optimización de procesos logísticos y tiempos de entrega",
        "Mejora continua en la experiencia del cliente",
        "Coordinación eficiente de múltiples procesos simultáneos",
        "Implementación exitosa de mejoras en procesos comerciales"
      ],
      
      companyInfo: {
        website: "#",
        industry: "Comercio y Servicios",
        size: "Mediana Empresa",
        logo: "/src/data/Logo/hello_there_logo.png"
      }
    },
    
    {
      id: "e-e-economia-estadistica",
      company: "E+E Economia y Estadistica para el Desarrollo",
      position: "Analista de Procesos y Control de Calidad de Datos (Proyectos Sociales y Educativos)",
      duration: "02/ene/2024 - 31/oct/2024",
      location: "Paraguay",
      type: "Proyecto",
      status: "completed",
      
      description: "Participé en procesos de selección y control de calidad en proyectos educativos y encuestas, liderando equipos y asegurando el cumplimiento de protocolos. Brindé soporte logístico y técnico para garantizar la integridad y confiabilidad de los datos.",
      
      responsibilities: [
        "Participación en procesos de selección y control de calidad",
        "Liderazgo de equipos en proyectos educativos",
        "Aseguramiento del cumplimiento de protocolos establecidos",
        "Soporte logístico y técnico para proyectos",
        "Garantía de integridad y confiabilidad de datos"
      ],
      
      technologies: [
        "Control de Calidad", "Análisis de Datos", "Gestión de Proyectos Sociales", 
        "Liderazgo de Equipos", "Protocolos de Calidad", "Soporte Logístico"
      ],
      
      achievements: [
        "Liderazgo exitoso de equipos en proyectos educativos",
        "Cumplimiento del 100% de protocolos de calidad establecidos",
        "Garantía de integridad y confiabilidad en el manejo de datos",
        "Implementación efectiva de soporte logístico y técnico"
      ],
      
      companyInfo: {
        website: "#",
        industry: "Investigación y Desarrollo Social",
        size: "Organización Especializada",
        logo: "/src/data/Logo/e_e_logo.png"
      }
    },
    
    {
      id: "freelance-reclutamiento",
      company: "Freelance",
      position: "Analista de Búsqueda y Selección",
      duration: "2025 - Presente",
      location: "Paraguay",
      type: "Freelance",
      status: "current",
      
      description: "Ejecuté y gestioné procesos completos de reclutamiento para perfiles de distintos niveles, desde el levantamiento del perfil hasta el feedback final, optimizando etapas, cumpliendo KPIs y garantizando una experiencia positiva y eficiente para candidatos y líderes.",
      
      responsibilities: [
        "Ejecución de procesos completos de reclutamiento y selección",
        "Levantamiento de perfiles para distintos niveles organizacionales",
        "Optimización de etapas del proceso de selección",
        "Cumplimiento de KPIs establecidos",
        "Garantía de experiencia positiva para candidatos y líderes",
        "Feedback final y seguimiento de procesos"
      ],
      
      technologies: [
        "Herramientas de Selección", "Herramientas de Sourcing", "LinkedIn Recruiter", 
        "Excel", "SuccessFactors", "SAP"
      ],
      
      achievements: [
        "Gestión exitosa de procesos de reclutamiento para múltiples perfiles",
        "Optimización eficiente de etapas del proceso de selección",
        "Cumplimiento consistente de KPIs y deadlines",
        "Mantenimiento de experiencia positiva para todos los stakeholders"
      ],
      
      companyInfo: {
        website: "#",
        industry: "Recursos Humanos",
        size: "Servicios Independientes",
        logo: "/src/data/Logo/freelance_logo.png"
      }
    }
  ],
  
  // Skills gained through work experience
  skillsGained: [
    "Reclutamiento y Selección",
    "Gestión de Procesos",
    "Atención al Cliente",
    "Control de Calidad",
    "Liderazgo de Equipos",
    "Análisis de Datos",
    "Sourcing",
    "Mejora Continua",
    "Gestión de Stakeholders",
    "Experiencia del Cliente"
  ],
  
  // Work statistics
  statistics: {
    totalProjects: 3,
    professionalPositions: 3,
    technologiesUsed: 15,
    yearsOfExperience: "4+",
    specializations: 2
  },
  
  // Call to action for work section
  callToAction: {
    title: "Trabajemos Juntos",
    description: "Siempre estoy interesada en nuevas oportunidades y proyectos desafiantes. Ya sea que necesites un analista de procesos, especialista en reclutamiento, o apoyo en proyectos de calidad, me encantaria escucharte.",
    buttonText: "Contáctame",
    buttonLink: "#contact"
  }
};