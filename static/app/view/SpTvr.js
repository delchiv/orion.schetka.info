
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
                allowBlank: false
            }
        },
        {
            text: 'Название',
            sortable: true,
            dataIndex: 'name',
            flex: 3,
            editor: {
                xtype: 'textfield',
                allowBlank: false
            }
        }
    ],
});