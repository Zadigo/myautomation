import _, { toNumber } from 'lodash'
import { defineStore } from 'pinia'
// import { useUtilities } from '@/composables/utils'
// TODO: Rename to custom_campaigns
import availableCampaigns from '@/data/available_campaigns.json'

const useCampaigns = defineStore('campaigns', {
  state: () => ({
    selectedCampaignSetup: {},
    availableCampaigns: availableCampaigns,
    currentCampaign: {},
    newCampaign: {
      name: null,
      urls: null,
      results_per_search: 100,
      csv_file: null,
      retries: 0,
      section_to_parse: null,
      parse_all_tables: false,
      parse_all_text: false,
      draft: true
    },
    campaigns: [],
  }),
  actions: {
    updateCampaigns (data) {
      // Update the list of campaigns 
      // and actions
      this.campaigns = data || []
    },
    setCurrentCampaign (campaign) {
      // Set the currently viewed 
      // campaign by reloading the
      // campaigns from the cache
      // if necessary
      this.loadFromCache()
      this.currentCampaign = campaign
    },
    loadFromCache (id = null) {
      // If there no campaigns on the store,
      // load the list of campaigns
      if (this.campaigns.length === 0) {
        this.updateCampaigns(this.$session.retrieve('cachedCampaigns'))
      }

      if (id) {
        const campaign = _.find(this.campaigns, ['id', toNumber(id)]) || {}
        this.currentCampaign = campaign
      }
    },
    useCampaignSetup (id) {
      this.selectedCampaignSetup = _.find(this.availableCampaigns, ['id', toNumber(id)])
    },
    resetNewCampaign () {
      this.newCampaign = {
        name: null,
        urls: null,
        results_per_search: 100,
        csv_file: null,
        retries: 0,
        section_to_parse: null,
        parse_all_tables: false,
        parse_all_text: false,
        draft: true
      }
    }
  },
  getters: {
    listActions () {
      return _.map(this.campaigns, (campaign) => {
        const result = {}
        _.forEach(campaign.actions, (action) => {
          result.id = action.id
          result.campaign_id = campaign.id
          result.campaign_name = campaign.name
          result.web_request = action.web_request
          result.url = action.url
          result.runned = action.runned
        })
        return result
      })
    }
  }
})

export {
  useCampaigns
}
