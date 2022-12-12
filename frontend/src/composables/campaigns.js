// import { useCampaigns }  from '@/store/campaigns'
import { client } from '@/plugins/axios'
import { ref } from 'vue'

export function useCampaignComposable () {
  const scrapResult = ref([])
  // const store = useCampaigns()

  // async function toggleCampaignState (campaign) {
  //   try {
  //     campaign.paused = !campaign.paused
  //     await client.post(`campaigns/${campaign.id}/state`)
  //     // store.updateCampaigns(response.data)
  //   } catch (error) {
  //     console.log(error)
  //   }
  // }

  async function launchCampaign (campaign) {
    try {
      campaign.paused = !campaign.paused
      campaign.runned = true
      const response = await client.post(`campaigns/run/${campaign.id}`)
      scrapResult.value = response.data
    } catch (error) {
      console.error(error)
    }
  }
  
  return {
    // toggleCampaignState,
    scrapResult,
    launchCampaign
  }
}
