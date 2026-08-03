// Education Data
export const educationData = {
  // Section configuration
  sectionId: "education",
  title: "Formación Académica",
  subtitle: "Mi trayectoria académica y cualificaciones",
  
  // Layout configuration
  layout: {
    wrapperClass: "wrapper style2",
    containerClass: "container",
    timelineClass: "timeline"
  },
  
  // Education entries (ordered by most recent first)
  institutions: [
    {
      id: "universidad-del-sol-psicologia",
      institution: "Universidad del Sol",
      shortName: "Universidad del Sol",
      degree: "Licenciatura en Psicología",
      duration: "2023 - 2027",
      location: "Paraguay",
      status: "ongoing",
      website: "#",
      logo: "/src/data/Logo/universidad_del_sol_logo.png",
      
      description: "Programa integral enfocado en la comprensión del comportamiento humano, procesos mentales y aplicaciones prácticas en ámbitos organizacionales y sociales.",
      
      highlights: [
        "Estudiante de tercer año con enfoque en Psicología Organizacional",
        "Especialización en procesos de selección y recursos humanos",
        "Aplicación práctica en proyectos de reclutamiento",
        "Desarrollo de habilidades en evaluación psicológica",
        "Participación en proyectos de investigación social"
      ],
      
      coursework: [
        "Psicología Organizacional",
        "Recursos Humanos", 
        "Evaluación Psicológica",
        "Psicología Social",
        "Métodos de Investigación",
        "Selección de Personal",
        "Comportamiento Organizacional",
        "Psicología Clínica"
      ]
    },
    
    {
      id: "universidad-autonoma-comercio",
      institution: "Universidad Autónoma de Asunción",
      shortName: "UAA",
      degree: "Licenciatura en Comercio Internacional",
      duration: "2010 - 2017",
      location: "Asunción, Paraguay",
      status: "completed",
      website: "#",
      logo: "/src/data/Logo/universidad_autonoma_logo.png",
      
      description: "Programa integral enfocado en comercio internacional, negocios globales y gestión empresarial con énfasis en mercados internacionales y relaciones comerciales.",
      
      highlights: [
        "Especialización en Comercio Internacional y Negocios Globales",
        "Desarrollo de habilidades en negociación y relaciones comerciales",
        "Formación en gestión empresarial y análisis de mercados",
        "Conocimientos en regulaciones comerciales internacionales",
        "Base sólida para transición a áreas de recursos humanos"
      ],
      
      coursework: [
        "Comercio Internacional",
        "Negocios Globales",
        "Gestión Empresarial",
        "Análisis de Mercados",
        "Negociación Comercial",
        "Economía Internacional",
        "Logística Internacional",
        "Finanzas Corporativas"
      ]
    }
  ],
  
  // Academic projects
  academicProjects: [
    {
      title: "Proyectos de Investigación en Psicología Social",
      institution: "Universidad del Sol",
      description: "Participación en proyectos de investigación enfocados en comportamiento organizacional y procesos de selección de personal",
      technologies: ["Métodos de Investigación", "Análisis Estadístico", "Evaluación Psicológica", "Herramientas de Selección"],
      highlights: [
        "Aplicación práctica de conocimientos teóricos",
        "Desarrollo de habilidades de investigación",
        "Enfoque en psicología organizacional",
        "Contribución a proyectos sociales y educativos"
      ]
    }
  ],
  
  // Academic achievements
  achievements: [
    {
      title: "Graduación en Comercio Internacional",
      year: "2017",
      placement: "Licenciada",
      description: "Graduación exitosa con especialización en negocios internacionales"
    },
    {
      title: "Estudiante Destacada en Psicología", 
      year: "2023-presente",
      placement: "Tercer Año",
      description: "Progreso académico exitoso con enfoque en psicología organizacional"
    }
  ],
  
  // Academic statistics
  statistics: {
    degreesCompleted: 1,
    degreesInProgress: 1,
    specializations: 2,
    yearsOfStudy: 10,
    practicalProjects: 3
  },
  
  // Learning goals
  learningGoals: [
    "Especialización avanzada en Psicología Organizacional",
    "Certificaciones en Recursos Humanos",
    "Técnicas avanzadas de reclutamiento y selección",
    "Herramientas digitales para HR",
    "Metodologías de evaluación psicológica",
    "Gestión del talento y desarrollo organizacional"
  ],
  
  // Call to action
  callToAction: {
    title: "Excelencia Académica",
    description: "Mi trayectoria educativa me ha proporcionado una base sólida en comercio internacional y psicología, combinando habilidades empresariales con comprensión del comportamiento humano.",
    buttonText: "Ver Habilidades",
    buttonLink: "#skills"
  }
};