const state = {
    httpOperator: require('axios').default,
    domain: `http://${location.hostname}:80`,
    dataSet: [],
    serverBusy: false,
    lastOperationMessage: "Application loaded",
    lastOperationStatus: null,

    totalNumberOfRecords: null,
    dataSource:null,
    units: null,

    viewPortSize:null
}

const getters = {
    getDataSet: (state) => {
        return state.dataSet
    },
    getServerBusy: (state) => {
        return state.serverBusy
    },
    getLastOperationStatus: (state) => {
        return state.lastOperationStatus
    },
    getLastOperationMessage: (state) => {
        return state.lastOperationMessage
    },
    getDataSource: (state) => {
        return state.dataSource
    },
    getTotalNumberOfRecords: (state) => {
        return state.totalNumberOfRecords
    },
    getUnits: (state) => {
        return state.units
    },
    getViewPortSize: (state) => {
        return state.viewPortSize
    }
}

const mutations = {
    setServerBusy: (state, value) => {
        state.serverBusy=value;
    },
    setLastOperationStatus: (state, value) => {
        state.lastOperationStatus = value;
    },
    setLastOperationMessage: (state, value) => {
        state.lastOperationMessage = value;
    },
    setDataSet: (state, value) => {
        state.dataSet = value
        // console.log("data set:" + state.dataSet)
    },
    setDataInfo: (state, value) => {
        // console.log("setting " + value)
        state.dataSource = value.source
        state.totalNumberOfRecords = value.totalRecords
        state.units = value.units
    },
    setViewPortSize: (state, value) => {
        state.viewPortSize = value
    }

}
const actions = {
    httpGetter: ({state}, payload) => {
        // console.log(`${state.domain}${payload}`)
        return  state.httpOperator.get(`${state.domain}${payload}`)
    },
    retrieveSeawaterData: ({commit, dispatch}) => {
        commit('setServerBusy', true);
        commit('setLastOperationStatus', null)
        commit('setLastOperationMessage', "Retrieving records")
        const link='/api/dataAccess/records/EMSO/58220'
        dispatch('httpGetter', link)
            .then((response) => {
            commit('setLastOperationMessage', 'Dataset retrieved successfully')
            commit('setLastOperationStatus', null)
            commit('setDataSet', response.data.message.data)
            commit('setDataInfo', {
                source: response.data.message.source,
                totalRecords: response.data.message.totalRecords,
                units: response.data.message.units
            })

        }).catch((alert) => {
            commit('setLastOperationMessage', alert.message)
            commit('setLastOperationStatus', 'error')
        }).finally(() => commit('setServerBusy', false))
    },
    calculateSalinity: ({commit, dispatch}) => {
        commit('setServerBusy', true);
        commit('setLastOperationStatus', null)
        commit('setLastOperationMessage', "Retrieving records with salinity calculated")

        const link='/api/dataAccess/records/EMSO/58220/salinity_calculated'
        dispatch('httpGetter', link)
            .then((response) => {
                commit('setLastOperationMessage', 'data loaded from csv')
                commit('setLastOperationStatus', null)
                // console.log(response.data.message.data)
                commit('setDataSet', response.data.message.data)
            }).catch((alert) => {
                commit('setLastOperationMessage', alert.message)
                commit('setLastOperationStatus', 'error')
            }).finally(() => commit('setServerBusy', false))
    }
}

export default {
    namespaced: true,
    state,
    getters,
    mutations,
    actions
}
