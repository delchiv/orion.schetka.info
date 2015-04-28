
Ext.define('Orion.view.rawm.PrihodDoc', {
    extend: 'Orion.view.base.PlainGridPanel',
    id:    'id-rawm-prihod-doc',
    xtype: 'rawm-prihod-doc',
    alias: 'widget.rawm-prihod-doc',

    columns: [
        {
            text: 'Дата',
            sortable: true,
            dataIndex: 'date',
            editor: {
                xtype: 'datefield',
            }
        },
        {
            text: '№',
            sortable: true,
            dataIndex: 'num',
            editor: {
                xtype: 'textfield',
                allowBlank: true,
            }
        },
        {
            text: 'Примечание',
            sortable: true,
            dataIndex: 'prim',
            flex: 1,
            editor: {
                xtype: 'textfield',
                allowBlank: true,
            }
        },
    ],
});

Ext.define('Orion.view.rawm.PrihodTvr', {
    extend: 'Orion.view.base.PlainGridPanel',
    id:    'id-rawm-prihod-tvr',
    xtype: 'rawm-prihod-tvr',
    alias: 'widget.rawm-prihod-tvr',

    autoLoad: false,

    columns: [
        {
            text: 'doc',
            sortable: true,
            dataIndex: 'doc',
        },
        {
            text: '№',
            sortable: true,
            dataIndex: 'num',
            editor: {
                xtype: 'textfield',
                allowBlank: true,
            }
        },
        {
            xtype: 'spcolumn',
            text: 'Компонент',
            sortable: true,
            flex: 1,

            dataIndex: 'tvr_kt',
            dataRenderIndex: 'tvr_kt__name',

            editor: {
                spUrl: '/components/',
                spDisplayField: 'name',
                spValueField: 'id',
            }
        },
        {
            text: 'К-во',
            sortable: true,
            dataIndex: 'k',
            flex: 1,
            editor: {
                xtype: 'numberfield',
                allowBlank: true,
            }
        },
        {
            text: 'Цена',
            sortable: true,
            dataIndex: 'с',
            flex: 1,
            editor: {
                xtype: 'numberfield',
                allowBlank: true,
            }
        },
        {
            text: 'Сумма',
            sortable: true,
            dataIndex: 's',
            flex: 1,
            editor: {
                xtype: 'numberfield',
                allowBlank: true,
            }
        },
    ],
});


Ext.define('Orion.view.rawm.Prihod', {
    extend: 'Ext.container.Container',
    xtype: 'rawm-prihod',
    layout: {
        type: 'vbox',
        align: 'stretch'
    },

    master: 'id-rawm-prihod-doc',
    detail: 'id-rawm-prihod-tvr',

    items: [
        { region: 'north', xtype: 'rawm-prihod-doc', height: 300 },
        { xtype: 'splitter' },
        { region: 'south', xtype: 'rawm-prihod-tvr', maintainFlex: true, flex: 1 },
    ],

    initComponent: function () {
        var me = this;
        me.callParent(arguments);

        Ext.getCmp(me.master).addListener('select', function (grid, record, index, eOpts) {
            var doctvr_grid = Ext.getCmp(me.detail);
            var id = parseInt(record.id);
            if (!id) { id = 0 };
            doctvr_grid.emptyRecord = {'doc':id,}
            console.log(doctvr_grid.emptyRecord);
            doctvr_grid.getStore().getProxy().api.read = '/doctvr/'+id+'/';
            doctvr_grid.getStore().reload();
        });
    },
});
