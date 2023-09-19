<template>
	<div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
		<div class="main-left col-span-1">
			<MyProfile />
		</div>
		<div class="main-center col-span-2 space-y-4">
			<div class="bg-white border border-gray-200 rounded-lg">
				<form
					class="space-y-1"
					method="post"
					v-on:submit.prevent="createPost">
					<div class="p-4 pb-1">
						<input
							type="text"
							class="p-4 w-50 h-4 bg-gray-100 rounded-full"
							v-model="postTitle"
							placeholder="add a title"
							maxlength="50" />
					</div>
					<div
						v-if="titleError"
						class="m-4 p-4 pb-1 pt-1 gap-4 text-gray-300 bg-red-500 rounded-lg">
						{{ titleError }}
					</div>
					<div class="p-4 pb-1 pt-1">
						<textarea
							class="p-4 w-full bg-gray-100 rounded-lg"
							v-model="postBody"
							placeholder="What are you thinking about?"></textarea>
					</div>
					<div class="p-4 border-t border-gray-100 flex justify-between">
						<a
							href="#"
							class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg"
							>Attach image</a
						>
						<button
							href="#"
							class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">
							Post
						</button>
					</div>
				</form>
			</div>
			<FeedItem
				v-for="post in posts"
				v-bind:key="post.id"
				v-bind:post="post" />
		</div>
		<div class="main-right col-span-1 space-y-4">
			<PeopleYouMayKnow />
			<Trends />
		</div>
	</div>
</template>

<script>
	import MyProfile from '@/components/common/MyProfile.vue';
	import FeedItem from '@/components/feed/FeedItem.vue';
	import PeopleYouMayKnow from '@/components/feed/PeopleYouMayKnow.vue';
	import Trends from '@/components/feed/Trends.vue';

	import axios from 'axios';
	import { useUserStore } from '../../stores/user';

	export default {
		name: 'FeedView',
		components: {
			MyProfile,
			PeopleYouMayKnow,
			Trends,
			FeedItem,
		},
		data() {
			const userStore = useUserStore();

			return {
				posts: [],
				postBody: '',
				postTitle: '',
				titleError: '',
				userId: userStore.user.id,
			};
		},
		mounted() {
			this.fetchFeed();
		},
		methods: {
			fetchFeed() {
				axios
					.get(`/api/v1/users/${this.userId}/posts/feed`)
					.then((response) => {
						this.posts = response.data;
						console.log(response);
					})
					.catch((error) => {
						console.error(error);
						console.warn('Error getting feed');
					});
			},
			// createPost() {
			// 	axios
			// 		.post('/api/v1/posts/', {
			// 			title: this.postTitle,
			// 			body: this.postBody,
			// 		})
			// 		.then((response) => {
			// 			console.log(response);
			// 			this.body = '';
			// 			this.posts.unshift(response.data);
			// 		})
			// 		.catch((error) => {
			// 			console.error('ERROR', error);
			// 			this.titleError = error.response.data.title[0];
			// 		});
			// },
		},
	};
</script>
