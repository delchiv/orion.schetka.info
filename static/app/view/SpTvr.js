
var storeSpGrp = new Ext.data.Store({
    autoLoad: true,
    fields: [], 
    proxy: {
        type: 'ajax',
        url: '/spgrp/',
        reader: {
            type: 'json',
            rootProperty: 'results'
        }
    }
});

Ext.define('Orion.view.SpTvr', {
    extend: 'Orion.view.base.PlainGridPanel',
    xtype: 'sptvr',
    alias: 'widget.sptvr',

    columns: [
        {
            text: 'Код',
            dataIndex: 'num',
            editor: {
                xtype: 'textfield',
                allowBlank: true,
            }
        },
        {
            text: 'Название',
            sortable: true,
            dataIndex: 'name',
            flex: 2,
            editor: {
                xtype: 'textfield',
                allowBlank: true,
            }
        },
        {
            text: 'Группа',
            sortable: true,
            flex: 2,
            dataIndex: 'grp',
            editor: new Ext.form.field.ComboBox({
                typeAhead: true,
                triggerAction: 'all',
                store: storeSpGrp,
                displayField: 'name',
                valueField: 'id',
            }),
            renderer: function(value, metaData, record, rowIndex, colIndex, store, view) {
                var data = record.data['grp_name'];
                return  data !== null ? data : '';
            }
        },
    ],
});