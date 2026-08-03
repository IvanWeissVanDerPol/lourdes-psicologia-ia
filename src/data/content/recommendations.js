// Professional Recommendations Data
export const recommendationsData = {
  // Section configuration
  sectionId: "recommendations",
  title: "Recommendations",
  subtitle: "What colleagues say about working with me",
  
  // Layout configuration
  layout: {
    wrapperClass: "wrapper style2 fade-up",
    containerClass: "container"
  },
  
  // Recommendations list
  recommendations: [
    {
      id: "monika-koykova",
      text: "Ivan demonstrates a proactive approach to problem-solving, preferring to tackle challenges independently while actively incorporating AI tools to enhance workflow efficiency. He shows enthusiasm in training sessions and coding, strives for knowledge, and is always willing to assist his team, including creating helpful scripts. For his level, he excels technically and is unafraid to use generative AI, which has also helped me learn new techniques for my day-to-day testing.",
      author: "Monika Koykova",
      position: "Senior Quality Assurance Lead",
      company: "MentorMate",
      companyLogo: "/src/data/Logo/mentormate_logo.jpeg",
      linkedIn: "#",
      date: "2024",
      skills: ["Problem Solving", "AI Tools", "Team Support", "Technical Excellence", "Knowledge Sharing"]
    },
    {
      id: "sarah-johnson",
      text: "I think Ivan is INCREDIBLY smart and talented. He thinks things through, has some automation and electrical/mechanical skills, and can analyze things well. I really enjoyed working with Ivan. As part of the Pelvital project team, he has demonstrated that he is really attentive to details, willing to help and support team members, always positive and polite, and has never been late to meetings. Yesterday, we had a conversation about a Jira ticket to be created, and Ivan sent me so much detailed and structured information about this case that creating a story would not be a problem at all. Ivan has a teamwork mindset.",
      author: "Sarah Johnson",
      position: "Business Analyst",
      company: "MentorMate",
      companyLogo: "/src/data/Logo/mentormate_logo.jpeg",
      linkedIn: "#",
      date: "2024",
      skills: ["Analytical Skills", "Attention to Detail", "Team Collaboration", "Communication", "Reliability"]
    },
    {
      id: "hugo-medina",
      text: "He worked with his tickets quickly and efficiently. He always maintained direct, fluid, and cordial communication with the author of the ticket. Ivan has a never-ending amount of energy and desire to learn and improve. When he finds a task interesting, he can go above and beyond to deliver. He is a techie with a preference for all back-end related things, and if there is a chance Python or anything related to automation can be used, he is on it, and you know he will deliver.",
      author: "Hugo Medina",
      position: "Software Development Engineer",
      company: "MentorMate",
      companyLogo: "/src/data/Logo/mentormate_logo.jpeg",
      linkedIn: "#",
      date: "2024",
      skills: ["Efficiency", "Communication", "Python", "Backend Development", "Automation"]
    },
    {
      id: "kalina-petrova",
      text: "In the project, Ivan took the initiative to help with the testing of the controller data, which wasn't an easy task to do. He had a lot of insights about that and helped the team a lot.",
      author: "Kalina Petrova",
      position: "Quality Assurance Specialist",
      company: "MentorMate",
      companyLogo: "/src/data/Logo/mentormate_logo.jpeg",
      linkedIn: "#",
      date: "2024",
      skills: ["Initiative", "Testing", "Team Support", "Technical Insights"]
    }
  ],
  
  // Key themes from recommendations
  keyThemes: [
    {
      theme: "Technical Excellence",
      mentions: 4,
      icon: "fa-star"
    },
    {
      theme: "Team Collaboration",
      mentions: 4,
      icon: "fa-users"
    },
    {
      theme: "Proactive Problem Solving",
      mentions: 3,
      icon: "fa-lightbulb"
    },
    {
      theme: "AI & Automation",
      mentions: 3,
      icon: "fa-robot"
    },
    {
      theme: "Communication Skills",
      mentions: 3,
      icon: "fa-comments"
    }
  ],
  
  // Statistics
  statistics: {
    totalRecommendations: 4,
    averageRating: 5.0,
    keySkillsMentioned: 20,
    companiesRepresented: 1
  }
};