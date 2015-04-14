
Ext.define('Orion.view.RowEditor', {
    extend: 'Ext.grid.plugin.RowEditing',
    alias: 'plugin.roweditor',

    clicksToMoveEditor: 2,
    autoCancel: true,
    listeners: {
        cancelEdit: function(rowEditing, context) {
            if (context.record.phantom) {
                context.store.remove(context.record);
            }
        },
        edit: function (rowEditing, context, eOpts) {
            context.store.sync();
        }
    }
})

Ext.define('Orion.view.base.PlainGridPanel', {
    extend: 'Ext.grid.Panel',

    requires: [
        'Orion.view.base.PlainGridPanelController'
    ],
    controller: 'base',

    tbar: {
        items: [
            {
                xtype: 'button',
                reference: 'newRecordButton',
                text: 'Добавить',
                handler: 'onNewButtonClick'
            },
            {
                xtype: 'button',
                reference: 'deleteRecordButton',
                text: 'Удалить',
                handler: 'onDeleteButtonClick',
                disabled:true
            }
        ]
    },

    selType: 'rowmodel',

    plugins: [
        'roweditor',
    ],

    listeners: {
        select: function (selModel, selections) {
            this.lookupReference('deleteRecordButton').setDisabled(false);
        }
    },

    initComponent: function() {
        var me = this;

        me.columns = Ext.Array.merge([
            {
                text: 'ID',
                hidden: false,
                dataIndex: 'id',
                renderer: function(v, meta, rec) {
                    return rec.phantom ? '' : v;
                }
            }
        ], me.columns);

        var field_list = [];
        Ext.each(me.columns, function () {
            var item = Ext.create ('Ext.data.Field', { name: this.dataIndex });
            field_list.push(item);
        });

        me.store = Ext.create('Orion.store.Base', { fields: field_list });
        me.store.getProxy().setUrl('/'+me.xtype.replace('-grid', '')+'/');

        me.callParent(arguments);
    }
});
