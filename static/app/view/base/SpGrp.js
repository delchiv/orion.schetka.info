
Ext.define('Orion.view.base.SpGrp', {
    extend: 'Orion.view.base.PlainGridPanel',
    xtype: 'spgrp',
    alias: 'widget.spgrp',

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
    ],
});