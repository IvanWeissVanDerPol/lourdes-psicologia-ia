// Scripts and external libraries data
export const scripts = {
  // Core JavaScript files (in order of loading)
  core: [
    {
      src: "/assets/js/jquery.min.js",
      type: "inline",
      required: true
    },
    {
      src: "/assets/js/jquery.scrolly.min.js", 
      type: "inline",
      required: true
    },
    {
      src: "/assets/js/jquery.scrollex.min.js",
      type: "inline", 
      required: true
    },
    {
      src: "/assets/js/browser.min.js",
      type: "inline",
      required: true
    },
    {
      src: "/assets/js/breakpoints.min.js",
      type: "inline",
      required: true
    },
    {
      src: "/assets/js/util.js",
      type: "inline",
      required: true
    },
    {
      src: "/assets/js/main.js",
      type: "inline",
      required: true
    }
  ],
  
  // External libraries
  external: [
    {
      name: "SAL.js",
      description: "Scroll Animation Library",
      css: "https://unpkg.com/sal.js@0.8.5/dist/sal.css",
      js: "https://unpkg.com/sal.js@0.8.5/dist/sal.js",
      config: {
        threshold: 0.2,
        once: true,
        duration: 600
      },
      initCode: `
        document.addEventListener('DOMContentLoaded', function() {
          if (typeof sal !== 'undefined') {
            sal({
              threshold: 0.2,
              once: true,
              duration: 600
            });
          }
        });
      `
    }
  ],
  
  // CSS files
  stylesheets: [
    {
      href: "/assets/css/main.css",
      type: "local",
      required: true
    },
    {
      href: "https://unpkg.com/sal.js@0.8.5/dist/sal.css",
      type: "external",
      name: "SAL.js CSS"
    }
  ]
}; 