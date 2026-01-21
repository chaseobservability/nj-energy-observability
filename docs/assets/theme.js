(function () {
  "use strict";

  var storageKey = "njobs-theme";
  var root = document.documentElement;

  function applyTheme(value, button) {
    if (value === "light" || value === "dark") {
      root.setAttribute("data-theme", value);
    } else {
      root.removeAttribute("data-theme");
    }
    if (button) {
      var label = value === "light" ? "Light" : value === "dark" ? "Dark" : "System";
      button.textContent = "Theme: " + label;
      button.setAttribute("aria-pressed", value === "light" || value === "dark");
    }
  }

  function ensureButton() {
    var button = document.getElementById("theme-toggle");
    if (button) {
      return button;
    }
    button = document.createElement("button");
    button.id = "theme-toggle";
    button.type = "button";
    button.className = "theme-toggle";
    button.setAttribute("aria-pressed", "false");
    button.textContent = "Theme: System";

    var target =
      document.querySelector(".site-nav .trigger") ||
      document.querySelector(".site-header .wrapper") ||
      document.querySelector(".site-header") ||
      document.querySelector(".site-footer .wrapper") ||
      document.querySelector(".site-footer") ||
      document.body;

    target.appendChild(button);
    return button;
  }

  function init() {
    var button = ensureButton();
    var saved = localStorage.getItem(storageKey);
    applyTheme(saved, button);

    button.addEventListener("click", function () {
      var current = localStorage.getItem(storageKey);
      var next = current === "light" ? "dark" : current === "dark" ? "" : "light";
      if (next === "") {
        localStorage.removeItem(storageKey);
        applyTheme(null, button);
      } else {
        localStorage.setItem(storageKey, next);
        applyTheme(next, button);
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
