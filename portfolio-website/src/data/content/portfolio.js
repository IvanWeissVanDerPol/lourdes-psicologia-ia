// Portfolio projects data
export const portfolioData = {
  // Section configuration
  sectionId: "projects",
  title: "My Projects",
  subtitle: "A showcase of my development work and learning journey",
  
  // Featured projects
  projects: [
    {
      id: "portfolio-website",
      title: "Portfolio Website",
      description: "Modern portfolio website built with Astro featuring component-based architecture, data-driven design, and GitHub Pages deployment. Demonstrates proficiency in static site generation, responsive design, and modern web development practices.",
      category: "Web Development",
      technologies: ["Astro", "JavaScript", "SCSS", "HTML5", "SAL.js", "GitHub Actions"],
      image: "/images/programmer.jpg", // Using existing image as placeholder
      liveUrl: "https://alcabvaldo.github.io",
      githubUrl: "https://github.com/alcabvaldo/alcabvaldo.github.io",
      featured: true,
      status: "completed",
      highlights: [
        "Component-based architecture with Astro",
        "Data-driven content management system",
        "Responsive design with mobile-first approach",
        "GitHub Pages deployment with CI/CD",
        "Performance optimized with minimal JavaScript"
      ]
    },
    {
      id: "university-projects",
      title: "Computer Science Coursework",
      description: "Collection of academic projects demonstrating fundamental computer science concepts including algorithms, data structures, and software engineering principles. Projects span multiple programming languages and problem domains.",
      category: "Academic",
      technologies: ["Python", "Java", "C++", "Algorithms", "Data Structures"],
      image: "/images/pic01.jpg", // Using existing image as placeholder
      githubUrl: "https://github.com/alcabvaldo/cs-coursework",
      featured: true,
      status: "ongoing",
      highlights: [
        "Algorithm implementation and analysis",
        "Data structure design and optimization",
        "Object-oriented programming patterns",
        "Problem-solving methodology",
        "Clean code practices and documentation"
      ]
    },
    {
      id: "web-development-demos",
      title: "Web Development Practice",
      description: "Various web development projects exploring different frameworks, libraries, and techniques. Includes responsive layouts, interactive components, and modern JavaScript applications.",
      category: "Web Development", 
      technologies: ["React", "Vue.js", "Node.js", "Express", "MongoDB"],
      image: "/images/pic02.jpg", // Using existing image as placeholder
      githubUrl: "https://github.com/alcabvaldo/web-development-practice",
      featured: false,
      status: "ongoing",
      highlights: [
        "Frontend framework exploration",
        "Backend API development",
        "Database integration",
        "User interface design",
        "Progressive web app features"
      ]
    },
    {
      id: "programming-challenges",
      title: "Algorithm Challenges",
      description: "Solutions to programming challenges from various platforms. Focus on algorithmic thinking, code optimization, and problem-solving strategies across different difficulty levels.",
      category: "Algorithms",
      technologies: ["Python", "JavaScript", "Java", "C++"],
      image: "/images/pic03.jpg", // Using existing image as placeholder
      githubUrl: "https://github.com/alcabvaldo/programming-challenges",
      featured: false,
      status: "ongoing",
      highlights: [
        "Competitive programming solutions",
        "Algorithm optimization techniques",
        "Data structure applications",
        "Time and space complexity analysis",
        "Multiple language implementations"
      ]
    }
  ],
  
  // Project categories for filtering
  categories: [
    {
      name: "All",
      filter: "*",
      active: true
    },
    {
      name: "Web Development",
      filter: "web-development",
      active: false
    },
    {
      name: "Academic",
      filter: "academic",
      active: false
    },
    {
      name: "Algorithms",
      filter: "algorithms", 
      active: false
    }
  ],
  
  // GitHub statistics (can be populated via API)
  githubStats: {
    publicRepos: 12,
    totalCommits: 250,
    languagesUsed: 8,
    contributionStreak: 45
  },
  
  // Call to action
  callToAction: {
    title: "Want to collaborate?",
    description: "I'm always interested in working on new projects and learning from experienced developers.",
    buttonText: "Get in Touch",
    buttonLink: "#contact"
  },
  
  // Layout configuration
  layout: {
    wrapperClass: "wrapper style1",
    containerClass: "container",
    gridClass: "row gtr-uniform"
  }
};