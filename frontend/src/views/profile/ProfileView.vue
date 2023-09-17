<template>
	<div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
		<!-- <profile-left-board
			:profileId="profileId"
			:isMyProfile="isMyProfile" /> -->
		<!-- <ProfileMiddleFeed :profileId="profileId" />
		<ProfileRightSuggestions :profileId="profileId" /> -->
	</div>
</template>

<script>
	import ProfileLeftBoard from './ProfileLeftBoard.vue';
	// import ProfileMiddleFeed from './ProfileMiddleFeed.vue';
	// import ProfileRightSuggestions from './ProfileRightSuggestions.vue';

	import { useUserStore } from '@/stores/user';
	import axios from 'axios';

	export default {
		name: 'ProfileView',
		components: {
			ProfileLeftBoard,
			// ProfileMiddleFeed,
			// ProfileRightSuggestions,
		},
		props: {
			id: {
				type: String,
				required: true,
			},
		},
		setup(props) {
			return {
				profileId: props.id,
				userStore: useUserStore(),
			};
		},
		data() {
			return {
				posts: [],
				profile: {},
				isMyProfile: false, // Add this property
				isFriend: null,
				isRequestPending: false,
				isLoading: true,
			};
		},
		// watch: {
		// 	id() {
		// 		this.resetData();
		// 		this.profileId = this.id;
		// 		this.fetchProfile();
		// 		this.getPostsByUserId();

		// 		this.checkIfMyProfile();
		// 		if (!this.isMyProfile) {
		// 			console.log('Not my profile');
		// 			this.getFriendRequestStatus();
		// 		}
		// 		console.log('Profile ID changed');
		// 		console.log(this.profileId);
		// 		console.log(this.userStore.user.id);
		// 		console.log(this.isMyProfile);
		// 	},
		// },
		mounted() {
			console.log(this.id);
			console
			this.fetchProfile();
			// this.getPostsByUserId();
			// this.checkIfMyProfile(); // Check if it's the user's own profile on mount

			// if (!this.isMyProfile) {
			// 	this.getFriendRequestStatus();
			// }
		},
		methods: {
			fetchProfile() {
				axios
					.get(`/api/v1/user/${this.profileId}/`)
					.then((response) => {
						this.profile = response.data;
						console.log(this.profile);
					})
					.catch((error) => {
						console.error(error);
						console.warn('Error getting profile');
					});
			},
			// getPostsByUserId() {
			// 	axios
			// 		.get(`/api/v1/posts/user/${this.profileId}/`)
			// 		.then((response) => {
			// 			this.posts = response.data;
			// 		})
			// 		.catch((error) => {
			// 			console.error(error);
			// 			console.warn('Error getting feed');
			// 		});
			// },

			// checkIfMyProfile() {
			// 	// Compare the current user's ID with the profile's user ID
			// 	if (this.profileId === this.userStore.user.id) {
			// 		this.isMyProfile = true;
			// 	}
			// 	console.log(this.isMyProfile);
			// },
			// getFriendRequestStatus() {
			// 	axios
			// 		.get(`/api/v1/friend-requests/check-friendship/${this.profileId}/`)
			// 		.then((response) => {
			// 			console.log(response.data.response);
			// 			this.isFriend = response.data.response.is_friend;
			// 			this.isRequestPending = response.data.response.is_request_pending;
			// 			this.isLoading = false;
			// 		})
			// 		.catch((error) => {
			// 			console.error(error);
			// 			console.warn('Error getting relation status');
			// 			this.isLoading = false;
			// 		});
			// },
			// resetData() {
			// 	this.posts = [];
			// 	this.profile = {};
			// 	this.isMyProfile = false;
			// 	this.isFriend = null;
			// 	this.isRequestPending = false;
			// 	this.isLoading = true;
			// },
		},
	};
</script>
