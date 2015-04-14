
Ext.define('Orion.view.base.PlainGridPanelController', {
    extend: 'Ext.app.ViewController',
    alias: 'controller.base',

    onNewButtonClick: function (button, evt) {
        var grid = this.getView();
        var rowEditing = grid.editingPlugin;
        rowEditing.cancelEdit();

        grid.getStore().insert(0, {});

        rowEditing.startEdit(0, 0);
    },

    onDeleteButtonClick: function () {
        var grid = this.getView();
        var selection = grid.getSelectionModel().getSelection()[0];
        if (selection) {
            grid.getStore().remove(selection);
            grid.getStore().sync();
        }
        grid.lookupReference('deleteRecordButton').setDisabled(true);
    }
});
