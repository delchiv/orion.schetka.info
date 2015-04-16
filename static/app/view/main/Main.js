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

    afterRender: function (eOpts) {
        var me = this;

        var data = Ext.create('Orion.store.Base', {fields: [],});
        data.getProxy().setUrl('/menu/');

        data.load(function () {
            var menus = [];
            this.data.each(function (rec) {
                if (rec.data['level'] === 0) {
                    var menu = Ext.create('Ext.tree.Panel', {
                        title: rec.data['name'],
                        rootVisible: false,
                        listeners: {
                            itemdblclick: function (view, record, item, index, event, options) {
                                var mainPanel = Ext.getCmp('id-mainpanel');
                        
                                var newTab = mainPanel.items.findBy(function (tab) {
                                    return tab.title === record.get('text');
                                });
                        
                                if (!newTab) {
                                    newTab = mainPanel.add({
                                        xtype: record.get('className'),
                                        closable: true,
                                        title: record.get('text')
                                    });
                                }
                        
                                mainPanel.setActiveTab(newTab);
                            },
                        }
                    });
                    menus.push(menu);
                } else {
// TODO Тут обрабатывается только первый уровень дерева (нужно дорабатывать)
                    var root = menus.slice(-1)[0].getRootNode();
                    root.appendChild({
                        text: rec.data['name'],
                        className: rec.data['link'],
                        leaf: true
                    });
                }
            });
            me.add(menus);
        });

        me.callParent(arguments);
    },
});

Ext.define('Orion.view.main.Panel', {
    extend: 'Ext.tab.Panel',
    xtype: 'mainpanel',

    activeTab: 0,

    items: [
        {
            xtype: 'sebest',
            closable: false,
            title: 'Себестоимость',
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
            id: 'id-mainpanel',
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