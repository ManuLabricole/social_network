<template>
	<div
		v-if="isProfileFetched"
		class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
		<profile-left-board :profile="profile" />
		<profile-middle-feed :profileId="profile.id" />
	</div>
</template>

<script>
	import ProfileLeftBoard from './ProfileLeftBoard.vue';
	import ProfileMiddleFeed from './ProfileMiddleFeed.vue';
	// import ProfileRightSuggestions from './ProfileRightSuggestions.vue';

	import { useUserStore } from '@/stores/user';
	import axios from 'axios';

	export default {
		name: 'ProfileView',
		components: {
			ProfileLeftBoard,
			ProfileMiddleFeed,
			// ProfileRightSuggestions,
		},
		props: {
			id: {
				type: String,
				required: true,
			},
		},
		data() {
			return {
				userStore: useUserStore(),
				isProfileFetched: false,
				profile: {},
				isMyProfile: false,
			};
		},
		mounted() {
			this.fetchProfile();
			this.setIsMyProfile();
		},
		methods: {
			fetchProfile() {
				axios
					.get(`/api/v1/user/${this.id}/`)
					.then((response) => {
						this.profile = response.data;
						this.isProfileFetched = true;
						console.log('profileFetched', this.profile);
					})
					.catch((error) => {
						console.error(error);
						console.warn('Error getting profile');
					});
			},
			setIsMyProfile() {
				// Compare the current user's ID with the profile's user ID
				if (this.profile.id === this.userStore.user.id) {
					this.isMyProfile = true;
				}
				console.log('isMyProfile', this.isMyProfile);
			},
		},
	};
</script>
