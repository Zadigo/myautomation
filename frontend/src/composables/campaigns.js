import { useCampaigns }  from '@/store/campaigns'

export function useCampaignComposable () {
  const store = useCampaigns()

  updateCampaign () {
    store
    // pass
  }
  
  return {
    updateCampaign
  }
}

export default useCampaignComposable
