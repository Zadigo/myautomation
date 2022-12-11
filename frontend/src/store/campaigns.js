import _, { toNumber } from 'lodash'
import { defineStore } from 'pinia'
import { useUtilities } from '@/composables/utils'
import availableCampaigns from '@/data/available_campaigns.json'

const useCampaigns = defineStore('campaigns', {
  state: () => ({
    selectedCampaignSetup: {},
    availableCampaigns: availableCampaigns,
    newCampaign: {
      name: null,
      url: null,
      runned: false,
      paused: true,
      archived: false,
      draft: true
    },
    campaigns: [],
    actions: []
  }),
  actions: {
    createCampaign () {
      // Create a new scrapping campaign
      const { incrementLastId } = useUtilities()
      const value = incrementLastId(this.campaigns)
      this.newCampaign.id = value
      this.campaigns.push(this.newCampaign)
    },
    useCampaignSetup (id) {
      this.selectedCampaignSetup = _.find(this.availableCampaigns, ['id', toNumber(id)])
    }
  }
})

export {
  useCampaigns
}
