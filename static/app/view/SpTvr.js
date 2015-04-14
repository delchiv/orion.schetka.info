
Ext.define('Orion.view.SpComob', {
    extend: 'Ext.form.field.ComboBox',
    xtype: 'spcombo',
    typeAhead: true,
    triggerAction: 'all',
    store: new Ext.data.Store({autoLoad: true, fields: [], proxy: {type: 'ajax', url: '/spgrp/',}}),
    displayField: 'name',
    valueField: 'id'
});

Ext.define('Orion.view.SpTvr', {
    extend: 'Orion.view.base.PlainGridPanel',
    xtype: 'sptvr',
    alias: 'widget.sptvr',

    columns: [
        {
            text: 'Код',
            sortable: true,
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
            editor: {
                xtype: 'spcombo',
            },
            renderer: function(value, metaData, record, rowIndex, colIndex, store, view) {
                console.log(value);
//                var data = record.data['grp_name'];
//                return  data !== null ? data : '';
                return value['name']
            }
        },
    ],
});