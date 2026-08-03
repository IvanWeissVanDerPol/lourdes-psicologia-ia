# Data Structure Documentation

This folder contains **ALL** static content, configuration, and assets for the website. Every piece of text, link, image path, CSS class, and configuration has been completely extracted from the Astro components into organized data files.

## 📁 **Folder Structure**

```
src/data/
├── index.js                 # Main export hub - imports and exports all data
├── config/                  # Site configuration files
│   ├── site.js             # Site metadata, SEO, basic settings
│   └── theme.js            # Theme, animations, CSS classes
├── content/                 # All text content and information
│   ├── personal.js         # Basic personal information
│   ├── navigation.js       # Navigation menu items
│   ├── hero.js             # Hero section content (ALL text fragments)
│   ├── contact.js          # Contact section content
│   └── social.js           # Social media links
└── assets/                  # Asset references and configurations
    ├── images.js           # Image paths and alt texts
    └── scripts.js          # JavaScript files and library configs
```

## 🎯 **100% Data-Driven Components**

### **Complete Text Extraction**
ALL text content has been moved to data files, including small fragments like:
- ✅ "Hi. I'm" → `heroData.greeting`
- ✅ "I'm a" → `heroData.rolePrefix`  
- ✅ ", currently studying Computer Sciente at" → `heroData.roleIntroduction`
- ✅ "Find me on ..." → `contactData.title`
- ✅ "Contact" → `contactData.buttonText`

### **Zero Hardcoded Content**
Components now contain **NO hardcoded text, links, or paths**:

```astro
<!-- ✅ FULLY DATA-DRIVEN -->
<p>{heroData.rolePrefix} <strong>{heroData.role}</strong>{heroData.roleIntroduction} <a href={heroData.university.url}>{heroData.university.name}</a>.</p>

<!-- ❌ OLD HARDCODED VERSION -->
<p>I'm a <strong>Software Developer</strong>, currently studying Computer Sciente at <a href="https://www.pol.una.py/">FP-UNA</a>.</p>
```

## 🎯 **Simple Import Pattern**
All components import from the main index file:

```javascript
import { heroData, themeConfig, socialLinks } from '../data/index.js';
```

## 📝 **Granular Content Control**

### **Text Fragment Management**
You can now edit individual text pieces:

```javascript
// src/data/content/hero.js
export const heroData = {
  greeting: "Hello! I'm",           // Change greeting
  rolePrefix: "I work as a",        // Change role introduction
  roleIntroduction: " and I study", // Change connector text
  // ...
};
```

### **Complete Social Link Control**
```javascript
// src/data/content/social.js
export const socialLinks = {
  primary: [...],  // Hero section (2-3 main links)
  all: [...]      // Contact section (all social links)
};
```

### **Animation Configuration**
```javascript
// src/data/config/theme.js
animations: {
  hero: {
    container: { animation: "fade", duration: 800 },
    image: { animation: "slide-right", delay: 200 },
    // ...
  }
}
```

## 🔧 **Pure Component Architecture**

Components are now **structure-only** with zero content:

```astro
---
// ✅ Pure component - only imports data
import { heroData, themeConfig } from '../data/index.js';
---

<!-- Only structure, all content from data -->
<h1>{heroData.greeting} <strong class={themeConfig.classes.gradientText}>{heroData.name}</strong></h1>
```

## 🎨 **Benefits Achieved**

### **1. Atomic Content Control**
- Edit individual words without touching components
- Change text connectors (like "and", "at", ",") separately
- Fine-tune messaging without code changes

### **2. Perfect Separation of Concerns**
- **Components** = Structure + Layout + Logic
- **Data Files** = Content + Configuration + Assets
- **Zero mixing** of content and structure

### **3. Content Management Ready**
- Ready for CMS integration
- Translatable content structure
- Version-controlled content changes

### **4. Maintainer-Friendly**
- Non-developers can edit content safely
- Clear content organization
- Predictable file structure

## 📋 **Content Editing Examples**

### **Change the Hero Greeting:**
```javascript
// src/data/content/hero.js
greeting: "Welcome! I'm",  // Instead of "Hi. I'm"
```

### **Modify Role Description:**
```javascript
// src/data/content/hero.js
rolePrefix: "I work as a",           // Instead of "I'm a"
roleIntroduction: " while pursuing", // Instead of ", currently studying"
```

### **Update Contact Button:**
```javascript
// src/data/content/contact.js
buttonText: "Get In Touch",  // Instead of "Contact"
```

### **Add Navigation Item:**
```javascript
// src/data/content/navigation.js
mainMenu: [
  { label: "Top", href: "#top", active: true },
  { label: "About", href: "#about", active: true },  // New item
  { label: "Contact", href: "#contact", active: true }
]
```

## 🚀 **Current Status: Production Ready**

### **✅ Fully Extracted**
- Every text fragment moved to data files
- All CSS classes in theme configuration
- Complete animation settings
- All asset paths organized

### **✅ Verified Functionality**
- Build system working perfectly
- Website looks and functions identically
- All animations and interactions preserved
- Zero hardcoded content remaining

### **✅ Ready for Enhancement**
- LinkedIn profile data integration ready
- New sections can be added easily
- Content updates without code changes
- Scalable architecture in place

## 💡 **Advanced Usage**

### **Conditional Content Display:**
```javascript
// src/data/content/hero.js
showUniversityInfo: true,  // Toggle university display
showSocialLinks: true,     // Toggle social links
```

### **Content Variations:**
```javascript
// src/data/content/hero.js
greetings: {
  formal: "Good day! I'm",
  casual: "Hi there! I'm", 
  creative: "Hey! I'm"
},
currentGreeting: "casual"  // Switch between variations
```

### **Multi-language Ready:**
```javascript
// Future: src/data/content/hero.en.js, hero.es.js
const language = "en";
import(`./hero.${language}.js`);
```

---

## 🎉 **Achievement: 100% Data-Driven Website**

Your website is now **completely content-driven** with:
- ✅ **Zero hardcoded text** in components
- ✅ **Granular content control** down to individual words
- ✅ **Maintainable architecture** ready for growth
- ✅ **Professional structure** following best practices

Ready to integrate your LinkedIn data and expand the website! 🚀 