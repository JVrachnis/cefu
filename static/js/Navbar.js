var Navbar = {
    // Default id's for navbar togglers
    registerToggleId: 'toggle-register',
    loginToggleId: 'toggle-login',

    // The name of the active class in the navbar
    activeClass: 'active',

    // The name of the item list class in the navbar
    navbarItemsClass: 'items',

    // Registers all toggle events
    init: function() {
        $("#" + Navbar.registerToggleId).click(Navbar.togglePanel);
        $("#" + Navbar.loginToggleId).click(Navbar.togglePanel);
    },

    // Toggles the appropiate panel when a navbar item is clicked
    togglePanel: function(event) {
        clicked = $(event.target);

        if (!clicked.is('a'))
            clicked = clicked.parent();

        panelId = clicked.attr('id').replace('toggle-', '');
        panel = $("#" + panelId);

        Navbar.hideToggled();
        Navbar.hideForms();
        clicked.addClass(Navbar.activeClass);
        panel.show();
    },

    // Hides all active items in the navbar
    hideToggled: function(items) {
        $('.' + Navbar.navbarItemsClass).find('.' + Navbar.activeClass).each(function(index, item) {
            $(item).removeClass(Navbar.activeClass);
        });
    },

    // Hides all visible panel forms
    hideForms: function() {
        $('.form').each(function(index, item) {
            $(item).hide();
        });
    },
};
