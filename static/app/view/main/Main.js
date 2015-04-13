/**
 * This class is the main view for the application. It is specified in app.js as the
 * "autoCreateViewport" property. That setting automatically applies the "viewport"
 * plugin to promote that instance of this class to the body element.
 *
 * TODO - Replace this content of this view to suite the needs of your application.
 */

Ext.define('Orion.view.main.MainMenu', {
    extend: 'Ext.panel.Panel',
    xtype: 'mainmenu',
    title: 'Меню',

    width: 250,
    layout: {
        type: 'accordion',
        multi: false
    },
    collapsible: true,
    split: true,
});

Ext.define('Orion.view.main.Panel', {
    extend: 'Ext.tab.Panel',
    xtype: 'mainpanel',

    activeTab: 0,

    items: [
        {
            xtype: 'panel',
            closable: false,
            title: 'Финансы',
        },
    ]
});

Ext.define('Orion.view.main.Header', {
    extend: 'Ext.toolbar.Toolbar',
    xtype: 'appheader',

    items: [
        {
            xtype: 'tbfill'
        },
        {
            xtype: 'button',
            text: 'Выход',
            reference: 'logout',
            listeners: {
                click: function () {
                    Ext.Ajax.request({
                        url: '/api/auth/logout/',
                        method: 'POST',
                        success: function(response, opts) {
                            window.location.reload();
                        }
                    });
                }
            }
        }
    ]
});

Ext.define('Orion.view.main.Main', {
    extend:  'Ext.Panel',
    xtype: 'main',
    alias: 'widget.main',

    layout: 'border',
    plugins: ['viewport',],

    items: [
        {
            region: 'center',
            xtype: 'mainpanel',
        },
        {
            region: 'north',
            xtype: 'appheader',
        },
        {
            region: 'west',
            xtype: 'mainmenu',
            split: true,
        }
    ]
});