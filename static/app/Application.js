Ext.define('Orion.Application', {
    extend: 'Ext.app.Application',

    name: 'Orion',

    appFolder: '/static/app',

    stores: [
        // TODO: add global/shared stores here
    ],

    requires: [
        'Orion.helper.CrsfTokenHelper',
    ],

    views: [
        'main.Main',
        'login.Login',
        'SpTvr',
    ],

    init: function () {
        // TODO - Launch the application
        this.splashscreen = Ext.getBody().mask(
            'Загрузка...', 'splashscreen'
        );
    },

    launch: function () {
        Ext.getBody().unmask();
        Ext.Ajax.request({
            url: '/api/auth/user/',
            success: function(response, opts) {
                Ext.widget('main');
            },
            failure: function(response, opts) {
                Ext.widget('login');
            }
        });
    },
});