
Ext.define('Orion.view.login.Login', {
    extend: 'Ext.window.Window',

    xtype: 'login',
    alias: 'widget.login',

    requires: [
        'Orion.view.login.LoginController'
    ],
    controller: 'login',

    autoShow: true,
    height: 170,
    width: 360,
    layout: {
        type: 'fit',
    },
    title: 'Вход',
    closable: false,
    draggable: false,
    resizable: false,

    items: [
        {
            xtype: 'form',
            reference: 'form',
            bodyPadding: 15,
            defaults: {
                xtype: 'textfield',
                anchor: '100%',
                labelWidth: 90,
                allowBlank: false,
                msgTarget: 'under',

                listeners: {
                    specialkey: 'onTextFieldSpecialKey'
                }
            },

            items: [
                {
                    name: 'username',
                    fieldLabel: 'Пользователь',
                },
                {
                    inputType: 'password',
                    name: 'password',
                    fieldLabel: 'Пароль',
                }
            ]
        }
    ],

    dockedItems: [
        {
            xtype: 'toolbar',
            dock: 'bottom',
            items: [ 
                {
                    xtype: 'tbfill'
                },
                {
                    xtype: 'button',
                    formBind: true,
                    listeners: { click: 'onButtonClickSubmit' },
                    text: 'Вход'
                },
                {
                    xtype: 'button',
                    listeners: { click: 'onButtonClickCancel' },
                    text: 'Отмена'
                }
            ]
        }
    ]
});