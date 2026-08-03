// Main data export - central hub for all website content
// Import all data modules
import { siteConfig } from './config/site.js';
import { themeConfig } from './config/theme.js';
import { personalData } from './content/personal.js';
import { navigationData } from './content/navigation.js';
import { heroData } from './content/hero.js';
import { contactData } from './content/contact.js';
import { socialLinks } from './content/social.js';
import { aboutData } from './content/about.js';
import { skillsData } from './content/skills.js';
import { portfolioData } from './content/portfolio.js';
import { workData } from './content/work.js';
import { educationData } from './content/education.js';
import { certificationsData } from './content/certifications.js';
import { recommendationsData } from './content/recommendations.js';
import { images } from './assets/images.js';
import { scripts } from './assets/scripts.js';

// Export all data for components to use
export {
  siteConfig,
  themeConfig,
  personalData,
  navigationData,
  heroData,
  contactData,
  socialLinks,
  aboutData,
  skillsData,
  portfolioData,
  workData,
  educationData,
  certificationsData,
  recommendationsData,
  images,
  scripts
};

// Default export with all data
export default {
  site: siteConfig,
  theme: themeConfig,
  personal: personalData,
  navigation: navigationData,
  hero: heroData,
  contact: contactData,
  social: socialLinks,
  about: aboutData,
  skills: skillsData,
  portfolio: portfolioData,
  work: workData,
  education: educationData,
  certifications: certificationsData,
  recommendations: recommendationsData,
  images,
  scripts
}; 