
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
            xtype: 'spcolumn',
            text: 'Группа',
            sortable: true,
            flex: 2,

            dataIndex: 'grp',
            dataRenderIndex: 'grp__name',

            editor: {
                spUrl: '/spgrp/',
                spDisplayField: 'name',
                spValueField: 'id',
            }
        },
        {
            xtype: 'spcolumn',
            text: 'ПодГруппа',
            sortable: true,
            flex: 2,

            dataIndex: 'subgrp',
            dataRenderIndex: 'subgrp__name',

            editor: {
                spUrl: '/spgrp/',
                spDisplayField: 'name',
                spValueField: 'id',
            }
        },
    ],
});


Ext.define('Orion.view.Products', {
    extend: 'Orion.view.SpTvr',
    xtype: 'products',
    alias: 'widget.products',
});

Ext.define('Orion.view.Components', {
    extend: 'Orion.view.SpTvr',
    xtype: 'components',
    alias: 'widget.components',
});

