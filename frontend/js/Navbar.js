var Navbar = {
    registerToggleId: 'toggle-register',
    loginToggleId: 'toggle-login',
    activeClass: 'active',
    navbarItemsClass: 'items',

    init: function() {
        $("#" + Navbar.registerToggleId).click(Navbar.togglePanel);
        $("#" + Navbar.loginToggleId).click(Navbar.togglePanel);
    },

    togglePanel: function(event) {
        clicked = $(event.target);
        panelId = clicked.attr('id').replace('toggle-', '');
        panel = $("#" + panelId);

        Navbar.hideToggled();
        Navbar.hideForms();
        clicked.addClass(Navbar.activeClass);
        panel.show();
    },

    hideToggled: function(items) {
        $('.' + Navbar.navbarItemsClass).find('.' + Navbar.activeClass).each(function(index, item) {
            $(item).removeClass(Navbar.activeClass);
        });
    },

    hideForms: function() {
        $('.form').each(function(index, item) {
            $(item).hide();
        });
    },
};
