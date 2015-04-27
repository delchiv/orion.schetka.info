
Ext.define('Orion.view.sebest.Sebest', {
    extend: 'Ext.grid.Panel',
    xtype: 'sebest',
    alias: 'widget.sebest',

    store: new Ext.data.Store({
        autoLoad: true,
        fields: [],
        proxy: {
            type: 'rest',
            url: '/sebest/',
    
            reader: {
                type: 'json',
            },
        },
        groupField: 'tvr_dt__name',
    }),

    features: [{
        ftype: 'groupingsummary',
        groupHeaderTpl: '{name}',
        hideGroupedHeader: true,
        enableGroupingMenu: false,
        startCollapsed: true,
        showSummaryRow: true,
    }],

    columns: [
        {
            text: 'Товар',
            sortable: true,
            dataIndex: 'tvr_dt__name',
        },
        {
            text: 'Компонент',
            sortable: true,
            dataIndex: 'tvr_kt__name',
        },
        {
            text: 'К-во',
            sortable: true,
            dataIndex: 'k',
        },
        {
            header: 'Цена',
            columns: [
                {
                    text: 'Акт.',
                    sortable: true,
                    dataIndex: 'cena_akt',
                },
                {
                    text: 'Ост.',
                    sortable: true,
                    dataIndex: 'cena_ost',
                },

            ]
        },
        {
            header: 'Себестоимость',
            columns: [
                {
                    text: 'Акт.',
                    sortable: true,
                    dataIndex: 'sum_akt',
                    summaryType: 'sum',
                },
                {
                    text: 'Ост.',
                    sortable: true,
                    dataIndex: 'sum_ost',
                    summaryType: 'sum',
                },

            ]
        },
    ]
});