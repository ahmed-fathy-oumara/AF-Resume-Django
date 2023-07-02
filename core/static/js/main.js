
(function () {
  'use strict';

  /**
   * Lazy Loading Images
  */

  let options = {
    threshold: 1
  }

  const observer = new IntersectionObserver(imageObserver, options);
  function imageObserver(entries, observer) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        const img_src = img.dataset.src;
        console.log("Lazy loading ", img);
        img.src = img_src;
        observer.unobserve(img);
      }
    })
  }

  let imgs = document.querySelectorAll('img.lazy');
  imgs.forEach(img => {
    observer.observe(img);
  })

  
  /**
   * Add shadow effect to fixed to top navigation bar
  */

  var stickyNavbar = function () {
    var navbar = document.querySelector('.navbar.fixed-top');
    if (navbar == null) return;
    var navbarClass = navbar.classList,
      scrollOffset = 20;
    var navbarStuck = function navbarStuck(e) {
      if (e.currentTarget.pageYOffset > scrollOffset) {
        navbar.classList.add('navbar-stuck');
      } else {
        navbar.classList.remove('navbar-stuck');
      }
    };

    // On load
    window.addEventListener('load', function (e) {
      navbarStuck(e);
    });

    // On scroll
    window.addEventListener('scroll', function (e) {
      navbarStuck(e);
    });
  }();

  /**
   * Anchor smooth scrolling
   * @requires https://github.com/cferdinandi/smooth-scroll/
  */

  var smoothScroll = function () {
    var selector = '[data-scroll]',
      fixedHeader = '[data-scroll-header]',
      scroll = new SmoothScroll(selector, {
        speed: 800,
        speedAsDuration: true,
        offset: function offset(anchor, toggle) {
          return toggle.dataset.scrollOffset || 40;
        },
        header: fixedHeader,
        updateURL: false
      });
  }();

  /**
   * Animate scroll to top button in/off view
  */

  var scrollTopButton = function () {
    var element = document.querySelector('.btn-scroll-top'),
      scrollOffset = 600;
    if (element == null) return;
    var offsetFromTop = parseInt(scrollOffset, 10);
    window.addEventListener('scroll', function (e) {
      if (e.currentTarget.pageYOffset > offsetFromTop) {
        element.classList.add('show');
      } else {
        element.classList.remove('show');
      }
    });
  }();

  /**
   * Tooltip
   * @requires https://getbootstrap.com
   * @requires https://popper.js.org/
  */

  var tooltip = function () {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
      return new bootstrap.Tooltip(tooltipTriggerEl, {
        trigger: 'hover'
      });
    });
  }();

  /**
   * Input fields formatter
   * @requires https://github.com/nosir/cleave.js
  */

  var inputFormatter = function () {
    var input = document.querySelectorAll('[data-format]');
    if (input.length === 0) return;
    for (var i = 0; i < input.length; i++) {
      var inputFormat = input[i].dataset.format,
        blocks = input[i].dataset.blocks,
        delimiter = input[i].dataset.delimiter;
      blocks = blocks !== undefined ? blocks.split(' ').map(Number) : '';
      delimiter = delimiter !== undefined ? delimiter : ' ';
      switch (inputFormat) {
        case 'card':
          var card = new Cleave(input[i], {
            creditCard: true
          });
          break;
        case 'cvc':
          var cvc = new Cleave(input[i], {
            numeral: true,
            numeralIntegerScale: 3
          });
          break;
        case 'date':
          var date = new Cleave(input[i], {
            date: true,
            datePattern: ['m', 'y']
          });
          break;
        case 'date-long':
          var dateLong = new Cleave(input[i], {
            date: true,
            delimiter: '-',
            datePattern: ['Y', 'm', 'd']
          });
          break;
        case 'time':
          var time = new Cleave(input[i], {
            time: true,
            datePattern: ['h', 'm']
          });
          break;
        case 'custom':
          var custom = new Cleave(input[i], {
            delimiter: delimiter,
            blocks: blocks
          });
          break;
        default:
          console.error('Sorry, your format ' + inputFormat + ' is not available. You can add it to the theme object method - inputFormatter in src/js/theme.js or choose one from the list of available formats: card, cvc, date, date-long, time or custom.');
      }
    }
  }();

  /**
   * Form validation
  */

  var formValidation = function () {
    var selector = 'needs-validation';
    window.addEventListener('load', function () {
      // Fetch all the forms we want to apply custom Bootstrap validation styles to
      var forms = document.getElementsByClassName(selector);
      // Loop over them and prevent submission
      var validation = Array.prototype.filter.call(forms, function (form) {
        form.addEventListener('submit', function (e) {
          if (form.checkValidity() === false) {
            e.preventDefault();
            e.stopPropagation();
          }
          form.classList.add('was-validated');
        }, false);
      });
    }, false);
  }();

})();