
Ext.define('Orion.view.sebest.Cena', {
    extend: 'Orion.view.base.PlainGridPanel',
    xtype: 'cena',
    alias: 'widget.cena',

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

            dataIndex: 'tvr_kt',
            dataRenderIndex: 'tvr_kt__name',

            editor: {
                spUrl: '/components/',
                spDisplayField: 'name',
                spValueField: 'id',
            }
        },
        {
            text: 'Цена',
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