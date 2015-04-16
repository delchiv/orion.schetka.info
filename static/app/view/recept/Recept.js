
Ext.define('Orion.view.recept.ReceptDoc', {
    extend: 'Orion.view.base.PlainGridPanel',
    id:    'id-recept-doc',
    xtype: 'recept-doc',
    alias: 'widget.recept-doc',

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
            xtype: 'spcolumn',
            text: 'Товар',
            sortable: true,
            flex: 1,

            dataIndex: 'tvr_dt',
            dataRenderIndex: 'tvr_dt__name',

            editor: {
                spUrl: '/products/',
                spDisplayField: 'name',
                spValueField: 'id',
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

Ext.define('Orion.view.recept.ReceptTvr', {
    extend: 'Orion.view.base.PlainGridPanel',
    id:    'id-recept-tvr',
    xtype: 'recept-tvr',
    alias: 'widget.recept-tvr',

    autoLoad: false,

    columns: [
        {
            text: 'doc',
            sortable: true,
            dataIndex: 'doc',
        },
        {
            text: 'tvr_dt',
            sortable: true,
            dataIndex: 'tvr_dt',
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
    ],
});


Ext.define('Orion.view.recept.Recept', {
    extend: 'Ext.container.Container',
    xtype: 'recept',
    layout: {
        type: 'vbox',
        align: 'stretch'
    },

    master: 'id-recept-doc',
    detail: 'id-recept-tvr',

    items: [
        { region: 'north', xtype: 'recept-doc', height: 300 },
        { xtype: 'splitter' },
        { region: 'south', xtype: 'recept-tvr', maintainFlex: true, flex: 1 },
    ],

    initComponent: function () {
        var me = this;
        me.callParent(arguments);

        Ext.getCmp(me.master).addListener('select', function (grid, record, index, eOpts) {
            var doctvr_grid = Ext.getCmp(me.detail);
            var id = parseInt(record.id);
            if (!id) { id = 0 };
            doctvr_grid.emptyRecord = {'doc':id, 'tvr_dt':record.data['tvr_dt']}
            console.log(doctvr_grid.emptyRecord);
            doctvr_grid.getStore().getProxy().api.read = '/doctvr/'+id+'/';
            doctvr_grid.getStore().reload();
        });
    },
});
