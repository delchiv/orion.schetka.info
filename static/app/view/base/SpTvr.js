
Ext.define('Orion.view.base.SpTvr', {
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
