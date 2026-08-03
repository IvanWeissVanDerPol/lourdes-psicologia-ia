// Professional Certifications and Credentials Data
export const certificationsData = {
  // Section configuration
  sectionId: "certifications",
  title: "Certifications & Credentials",
  subtitle: "Professional certifications and academic achievements",
  
  // Layout configuration
  layout: {
    wrapperClass: "wrapper style2 fade-up",
    containerClass: "container"
  },
  
  // Professional Certifications (ordered by importance/recency)
  certifications: [
    {
      id: "istqb-foundation",
      title: "ISTQB Foundation Level Certification",
      issuer: "International Software Testing Qualifications Board (ISTQB)",
      issueDate: "2022",
      expiryDate: "No expiry",
      status: "active",
      credentialUrl: "/src/data/PersonalData/Certifications/Certifications/Personal/Certificate-8e85e79dd27d41078da9908a53aaedb8.pdf",
      verificationUrl: "https://www.istqb.org/",
      credentialId: "ISTQB-FL-2022",
      category: "Software Testing",
      logo: "/src/data/Logo/ISTQB_logo.png",
      
      description: "Achieved an industry-recognized certification in core software testing principles, covering test design techniques, execution strategies, and reporting methodologies. This certification highlights proficiency in both manual and automated testing, ensuring software quality through structured processes and best practices.",
      
      skills: [
        "Test Design Techniques", "Test Execution", "Test Reporting",
        "Manual Testing", "Automated Testing", "Software Quality"
      ],
      
      verified: true,
      badgeStyle: "certification",
      icon: "fa-bug",
      badgeColor: "primary"
    },
    
    {
      id: "nasa-galactic-problem-solver",
      title: "NASA Galactic Problem Solver",
      issuer: "NASA International Space Apps Challenge",
      issueDate: "2023",
      expiryDate: "Lifetime",
      status: "active",
      credentialUrl: "/src/data/PersonalData/Certifications/Certifications/Personal/NASA_International_Space_Apps_Challenge.jpg",
      verificationUrl: "https://2023.spaceappschallenge.org/",
      credentialId: "NASA-SPS-2023",
      category: "Innovation & AI",
      logo: "/src/data/Logo/nasa_space_logo.png",
      
      description: "Awarded the Galactic Problem Solver title at the NASA International Space Apps Challenge 2023 for pioneering solutions utilizing AI and automation. Recognized for addressing complex challenges in space exploration through innovative technological applications, contributing to NASA's global open innovation initiatives.",
      
      skills: [
        "Artificial Intelligence", "Automation", "Problem Solving",
        "Innovation", "Space Technology", "Open Innovation"
      ],
      
      verified: true,
      badgeStyle: "award",
      icon: "fa-rocket",
      badgeColor: "accent"
    },
    
    {
      id: "becal-english-scholarship",
      title: "Advanced English Proficiency (BECAL Scholarship Recipient)",
      issuer: "BECAL Scholarship Program",
      issueDate: "2021",
      expiryDate: "Lifetime",
      status: "completed",
      credentialUrl: "/src/data/PersonalData/Certifications/Certifications/Personal/Ivan_Weiss_Advanced_English_Proficiency_Certificate_BECAL_Scholarship_2022.jpg",
      verificationUrl: "https://www.becal.gov.py/",
      credentialId: "BECAL-2021-IW",
      category: "Professional Development",
      logo: "/src/data/Logo/Becal_logo.jpg",
      
      description: "Awarded the prestigious BECAL Scholarship, a merit-based program funded by the Paraguayan government, to pursue advanced English studies. This scholarship provided an opportunity to enhance my professional communication skills and strengthen global collaboration abilities. As part of the program, I attended Wichita State University in the USA, further refining my language proficiency and participating in academic initiatives that broadened my international perspective.",
      
      skills: [
        "Advanced English", "Professional Communication", "International Collaboration",
        "Academic English", "Cross-cultural Communication", "Global Perspective"
      ],
      
      verified: true,
      badgeStyle: "scholarship",
      icon: "fa-globe",
      badgeColor: "secondary"
    },
    
    {
      id: "tau-test-automation",
      title: "TAU Test Automation Certifications",
      issuer: "Test Automation University",
      issueDate: "2022",
      expiryDate: "No expiry",
      status: "active",
      credentialUrl: "/src/data/PersonalData/Certifications/Certifications/Mentormate/Test_Automation_University/",
      verificationUrl: "https://testautomationu.applitools.com/",
      credentialId: "TAU-2022-IW",
      category: "Test Automation",
      logo: "/src/data/Logo/Tau_logo.png",
      
      description: "Comprehensive training in modern test automation techniques, frameworks, and best practices through multiple specialized courses.",
      
      courses: [
        "Test Automation University Foundations",
        "Python Programming for Automation",
        "Java Programming for Automation",
        "JavaScript Test Automation with WebdriverIO",
        "Introduction to Cypress",
        "Continuous Integration with Jenkins",
        "API Testing with Postman",
        "Behavior-Driven Development (BDD) with Cucumber",
        "Web Element Locator Strategies",
        "Selenium WebDriver with Java",
        "Advanced Selenium Techniques",
        "AI in Test Automation",
        "Visual Validation Testing with Applitools"
      ],
      
      skills: [
        "Test Automation", "Python", "Java", "JavaScript", "WebdriverIO",
        "Cypress", "Jenkins", "Postman", "BDD", "Cucumber", "Selenium",
        "AI Testing", "Visual Testing", "CI/CD"
      ],
      
      verified: true,
      badgeStyle: "certification",
      completedCourses: 13,
      icon: "fa-robot",
      badgeColor: "primary"
    }
  ],
  
  // Skill assessments and badges
  skillAssessments: [
    {
      id: "python-qa-automation",
      title: "Python for QA Automation",
      platform: "Test Automation University",
      status: "passed",
      badgeEarned: true,
      category: "Test Automation",
      
      description: "Comprehensive certification in Python programming for test automation and quality assurance.",
      
      icon: "fa-check-circle",
      badgeColor: "success"
    },
    {
      id: "api-testing-postman",
      title: "API Testing with Postman",
      platform: "Test Automation University",
      status: "passed",
      badgeEarned: true,
      category: "API Testing",
      
      description: "Advanced certification in API testing methodologies using Postman.",
      
      icon: "fa-check-circle",
      badgeColor: "success"
    }
  ],
  
  // Awards and recognitions
  awards: [
    {
      id: "nasa-space-apps",
      title: "NASA International Space Apps Challenge Winner",
      issuer: "NASA",
      issueDate: "October 2023",
      status: "completed",
      category: "Innovation",
      
      description: "Recognized as Galactic Problem Solver for innovative AI and automation solutions addressing space exploration challenges.",
      
      achievements: [
        "Developed innovative AI-powered solutions",
        "Addressed complex space exploration challenges",
        "Contributed to global open innovation initiatives",
        "Collaborated with international teams"
      ],
      
      icon: "fa-trophy",
      badgeColor: "gold"
    },
    {
      id: "becal-scholarship",
      title: "BECAL Merit Scholarship",
      issuer: "Paraguayan Government - BECAL Program",
      issueDate: "2021",
      status: "completed",
      category: "Academic Achievement",
      
      description: "Prestigious merit-based scholarship for advanced English studies and international academic exchange.",
      
      achievements: [
        "Selected based on academic excellence",
        "Funded international education at Wichita State University",
        "Enhanced professional and language skills",
        "Represented Paraguay internationally"
      ],
      
      icon: "fa-award",
      badgeColor: "gold"
    }
  ],
  
  // Certification statistics
  statistics: {
    totalCertifications: 15,
    activeCertifications: 14,
    categories: ["Software Testing", "Test Automation", "Innovation & AI", "Professional Development"],
    specializedCourses: 13,
    internationalRecognitions: 2
  },
  
  // Call to action
  callToAction: {
    title: "Continuous Learning",
    description: "I'm committed to staying current with industry trends and continuously expanding my professional capabilities through ongoing education and certification.",
    buttonText: "View LinkedIn Profile",
    buttonLink: "https://www.linkedin.com/in/ivanweissvanderpol/"
  }
};