
Ext.define('Orion.store.Base', {
    extend: 'Ext.data.Store',
    autoLoad: true,
    autoSync: false,
    proxy: {
        type: 'rest',
        url: '',

        reader: {
            type: 'json',
        },
        writer: {
            type: 'json',
            writeAllFields: true,
        }
    }
});