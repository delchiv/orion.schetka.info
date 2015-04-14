
Ext.define('Orion.store.Base', {
    extend: 'Ext.data.Store',
    autoLoad: true,
    autoSync: false,
    proxy: {
        type: 'rest',
        url: '',
        actionMethods: {create: 'POST', read: 'GET', update: 'PATCH', destroy: 'DELETE'},

        reader: {
            type: 'json',
            rootProperty: 'results'
        },
        writer: {
            type: 'json',
            writeAllFields: true
        }
    }
});