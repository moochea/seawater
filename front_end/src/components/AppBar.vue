<template>
    <v-app-bar
            app
            color="white"
            dark
            id="appbar"
    >
        <table width="100%">
            <tr>
                <td>
                    <v-img
                            alt="Seawater Conditions"
                            class="shrink mr-2"
                            contain
                            src="https://cdn2.iconfinder.com/data/icons/animals-133/64/animal_wildlife_bird_seagull-512.png"
                            transition="scale-transition"
                            width="70"
                    />
                </td>
                <td class="hidden-sm-and-down">
                    <div class="heading">
                        Seawater Conditions
                    </div>
                    <v-spacer></v-spacer>
                </td>
                <td width="50%">
                    <div :class=messageClass>
                        {{getLastOperationMessage}}
                    </div>
                </td>
                <td>
                    <div class="message">
                        <v-progress-circular
                                :indeterminate="getServerBusy"
                                :color=progressColor
                        >
                        </v-progress-circular>
                    </div>
                </td>
            </tr>
        </table>

    </v-app-bar>
</template>
<script>
    export default {
        name: 'AppBar',
        props: {
            getLastOperationMessage: {},
            getServerBusy: {},
            getLastOperationStatus: {}
        },
        data: () => ({
                         progressColor: "#dd1111",
                         messageClass: "message"
                     }),

        watch: {
            getLastOperationStatus(newValue){
                if (newValue === "error") {
                    this.messageClass = "errorMessage"
                }
                if (newValue === "warning") {
                    this.messageClass = "warningMessage"
                }
                if (!newValue) {
                    this.messageClass = "message"
                }

            }
        }
    }
</script>
<style>
    .heading {
        color: #000000;
        font-style: italic
    }

    .message {
        color: #000000;
        text-align: right;
        font-size: small;
    }
    .warningMessage {
        color: #aaaa00;
        text-align: right;
    }
    .errorMessage {
        color: #ff1111;
        text-align: right;
    }
</style>
