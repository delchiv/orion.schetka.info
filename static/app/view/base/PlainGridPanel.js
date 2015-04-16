
Ext.define('Orion.view.RowEditor', {
    extend: 'Ext.grid.plugin.RowEditing',
    alias: 'plugin.roweditor',

    clicksToMoveEditor: 2,
    autoCancel: true,
    listeners: {
        cancelEdit: function(editor, context, eOpts) {
            if (context.record.phantom) {
                context.store.remove(context.record);
            }
        },
        edit: function (editor, context, eOpts) {
            context.store.sync();
            context.record.commit();
        }
    }
})

Ext.define('Orion.view.SpColumn', {
    extend: 'Ext.grid.column.Column',
    xtype: 'spcolumn',

    initComponent: function() {
        var me = this;

        var editor = Ext.Object.merge({
            typeAhead: true,
            triggerAction: 'all',
            store: new Ext.data.Store({autoLoad: true, fields: [], proxy: {type: 'ajax', url: me.editor.spUrl,}}),
            displayField: me.editor.spDisplayField,
            valueField: me.editor.spValueField,
            dataRenderIndex: me.dataRenderIndex,
            listeners: {
                select: function (combo, record, eOpts) {
                    combo.column.container.component.grid.getSelection()[0].data[combo.dataRenderIndex] = record.data[combo.displayField];
                },
            }
        }, me.editor)


        me.editor = new Ext.form.field.ComboBox(editor);

        me.callParent(arguments);
    },

    renderer: function(value, metaData, record, rowIndex, colIndex, store, view) {
        var data = record.data[this.columns[colIndex].dataRenderIndex];
        return  data !== null ? data : '';
    },
})

Ext.define('Orion.view.base.PlainGridPanel', {
    extend: 'Ext.grid.Panel',

    autoLoad: true,
    emptyRecord: {},

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

        me.store = Ext.create('Orion.store.Base', { fields: field_list, autoLoad: this.autoLoad });
        var api = me.store.getProxy().api;
        var url = '/'+me.xtype.replace('-grid', '')+'/';
        api.create = url;
        api.read   = url;
        api.update = url;
        api.destroy = url;

        me.callParent(arguments);
    }
});
