<template>
	<div
		v-if="isProfileFetched"
		class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
		<profile-left-board
			:profile="profile"
			:isMyProfile="isMyProfile" />
		<profile-middle-feed :profile="profile" />
		<profile-right-suggestions :profile="profile" />
	</div>
</template>

<script>
	import ProfileLeftBoard from './ProfileLeftBoard.vue';
	import ProfileMiddleFeed from './ProfileMiddleFeed.vue';
	import ProfileRightSuggestions from './ProfileRightSuggestions.vue';

	import { useUserStore } from '@/stores/user';
	import axios from 'axios';

	export default {
		name: 'ProfileView',
		components: {
			ProfileLeftBoard,
			ProfileMiddleFeed,
			ProfileRightSuggestions,
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
				isMyProfile: false,
				isProfileFetched: false,
				profile: {},
			};
		},
		mounted() {
			this.fetchProfile();
			this.setIsMyProfile();
			console.log('ProfileView mounted');
			console.log(this.profile);
		},
		methods: {
			fetchProfile() {
				axios
					.get(`/api/v1/users/${this.id}/`)
					.then((response) => {
						this.profile = response.data;
						this.setIsMyProfile();
						this.isProfileFetched = true;
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
		watch: {
			id() {
				this.fetchProfile();
				this.setIsMyProfile();
			},
		},
	};
</script>
