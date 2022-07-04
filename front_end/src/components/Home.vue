<template>
    <v-card>
            <v-card id="descriptionCard" >
                <v-card-title>Dataset Viewer <v-spacer></v-spacer>
                    <v-btn class="hidden-md-and-up" @click="displayDescription=!displayDescription"><v-icon>mdi-swap-vertical</v-icon></v-btn>
                </v-card-title>
                <v-card-text v-if="displayDescription">This page retrieves and displays a selected EMSO dataset,
                    and calculates the practical salinity from conductivity,
                    according to the formula https://www.teos-10.org/pubs/gsw/html/gsw_SP_from_C.html
                    CSV data obtained from https://www.seanoe.org/data/00454/56528/
                </v-card-text>
                <table width="100%">
                    <tr>
                        <td>
                            <span class="note">
                                Data source: {{getDataSource}}
                            </span>
                        </td>
                        <td>
                            <span class="note">
                                Total number of Records: {{getTotalNumberOfRecords}}
                            </span>
                        </td>
                        <td>
                            <v-btn @click="refreshDataRetrieved">
                                <span class="hidden-sm-and-down">Refresh</span>
                                <v-icon>mdi-refresh</v-icon></v-btn>
                        </td>
                        <td>
                            <v-btn @click="startSalinityCalculations">
                                <span class="hidden-sm-and-down">Calculate</span>
                                <v-icon>mdi-calculator</v-icon>
                            </v-btn>
                        </td>
                    </tr>
                </table>
            </v-card>
            <v-card id="dataCard" >
                <v-data-table
                    :headers="headers"
                    :items="getDataSet"
                    :items-per-page="30"
                    fixed-header
                    :height="datasetCardHeight"
                    ></v-data-table>
            </v-card>
    </v-card>
</template>

<script>
    import {mapActions, mapGetters} from "vuex";


    export default {
        name: "Home",
        data: () => ({
            headers: [
                {text: 'Timestamp', value:'timestamp'},
                {text: 'Temperature', value:'temperature'},
                {text: 'Conductivity', value:'conductivity'},
                {text: 'Pressure', value:'pressure'},
                {text: 'EMSO salinity', value:'salinity'},
                {text: 'Practical salinity', value:'pSalinity'}
            ],
            datasetCardHeight: 400,
            paginationBarHeight: 63,
            displayDescription:true
        }),
        watch: {
            getViewPortSize(newValue) {
                this.adjustDataCardHeight(newValue.height)
            },
            getUnits(newValue) {
                if(newValue) {
                    this.headers = [
                        {text: 'Timestamp', value:'timestamp'},
                        {text: `Temperature (${this.getUnits.temperature})`, value:'temperature'},
                        {text: `Conductivity (${this.getUnits.conductivity})`, value:'conductivity'},
                        {text: `Pressure (${this.getUnits.pressure})`, value:'pressure'},
                        {text: `EMSO salinity (${this.getUnits.salinity})`, value:'salinity'},
                        {text: 'Practical salinity', value:'pSalinity'}
                    ]
                }
            }
        },
        updated() {
            this.adjustDataCardHeight(window.innerHeight)
        },
        computed: {
            ...mapGetters('commandStore', ['getDataSet', 'getLastOperationStatus', 'getLastOperationMessage',
                'getServerBusy', 'getTotalNumberOfRecords', 'getDataSource', 'getViewPortSize', 'getUnits'])
        },
        methods: {
            ...mapActions('commandStore', ['calculateSalinity', 'retrieveSeawaterData']),
            refreshDataRetrieved() {
                this.retrieveSeawaterData()
            },
            startSalinityCalculations(){
                this.calculateSalinity();
            },
            adjustDataCardHeight(newValue) {
                var middleCardHeight = document.getElementById("descriptionCard").offsetHeight;
                // console.log("middle card height: " + middleCardHeight)
                var appbarHeight = document.getElementById("appbar").clientHeight
                this.datasetCardHeight = newValue - middleCardHeight - appbarHeight - this.paginationBarHeight
            }
        },
        mounted() {
            this.adjustDataCardHeight(window.innerHeight)
            this.refreshDataRetrieved()
        }
    }
</script>
<style>
    .note {
        font-size: small;
    }
</style>

