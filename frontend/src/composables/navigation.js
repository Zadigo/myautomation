import { useCampaigns } from '@/store/campaigns'
import router from '@/router'

export function useNavigation (app) {
  const store = useCampaigns()

  function saveSession () {
    app.appContext.config.globalProperties.$session.create('draftCampaign', store.newCampaign)
  }

  function goToPrevious (params) {
    // Save the campaign in the user session. This stays until
    // the user completes all the steps and creates the campaign
    // app.appContext.config.globalProperties.$router.push(params)
    // this.$router.push({ name: 'campaign_setup_settings_view', params: { id: this.$route.params.id } })
    router.push(params)
    saveSession()
  }

  function goToNext (params) {
    // Save the campaign in the user session. This stays until
    // the user completes all the steps and creates the campaign
    // console.log(app)
    // app.appContext.config.globalProperties.$session.create('draftCampaign', this.store.newCampaign)
    // app.appContext.config.globalProperties.$router.push(params)
    // this.$router.push({ name: 'campaign_setup_settings_view', params: { id: this.$route.params.id } })
    router.push(params)
    saveSession()
  }

  return {
    goToPrevious,
    goToNext,
    saveSession
  }
}
