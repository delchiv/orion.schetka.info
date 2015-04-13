Ext.define('Orion.view.login.LoginController', {
    extend: 'Ext.app.ViewController',

    alias: 'controller.login',

    onButtonClickCancel: function (field, e, options) { this.lookupReference('form').reset(); },

    onButtonClickSubmit: function (field, e, options) { 
        var me = this;
        if (me.lookupReference('form').isValid()) {
            me.doLogin();
        };
    },

    onTextFieldSpecialKey: function (field, e, options) {
        console.log('ENTER');
        if (e.getKey() === e.ENTER) { 
            this.doLogin();
        }
    },

    doLogin: function () {
        var me = this;

        this.getView().mask('Авторизация...');

        Ext.Ajax.request({
            url: '/api/auth/login/',
            method: 'POST',
            params: me.lookupReference('form').getForm().getFieldValues(),
            success: function(response, opts) {
                me.getView().unmask();
                me.getView().destroy();
                Ext.widget('main').show();
            },
            failure: function(response, opts) {
                me.getView().unmask();
            }
        });
    },
});