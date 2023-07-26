```python
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

import UserProfile from './user_profile';
import RecommendationEngine from './recommendation_engine';
import ProductSearch from './product_search';
import AlertsOffers from './alerts_offers';
import WishlistFavorites from './wishlist_favorites';
import VoiceCommand from './voice_command';
import SocialSharing from './social_sharing';
import InAppPurchases from './in_app_purchases';

const Stack = createStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="UserProfile">
        <Stack.Screen name="UserProfile" component={UserProfile} />
        <Stack.Screen name="RecommendationEngine" component={RecommendationEngine} />
        <Stack.Screen name="ProductSearch" component={ProductSearch} />
        <Stack.Screen name="AlertsOffers" component={AlertsOffers} />
        <Stack.Screen name="WishlistFavorites" component={WishlistFavorites} />
        <Stack.Screen name="VoiceCommand" component={VoiceCommand} />
        <Stack.Screen name="SocialSharing" component={SocialSharing} />
        <Stack.Screen name="InAppPurchases" component={InAppPurchases} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
```