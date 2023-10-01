<template>
	<div v-if="comments.length > 0">
		<div
			v-for="comment in comments.slice(-5)"
			class="flex mt-4 items-center">
			<div
				:key="comment.id"
				class="flex items-center mb-3 flex-grow">
				<img
					src="https://i.pravatar.cc/300?img=70"
					class="w-10 h-10 rounded-full sm mr-4" />
				<div class="ml-3 bg-gray-100 rounded-lg p-2 flex-grow">
					<strong class="text-blue-600">{{ comment.author.user.name }}</strong>
					<p class="text-gray-700">{{ comment.content }}</p>
				</div>
			</div>
		</div>
	</div>
	<div v-if="!userHasCommented">
		<div class="flex items-center mt-3">
			<img
				src="https://i.pravatar.cc/300?img=70"
				class="w-10 h-10 rounded-full" />
			<textarea
				v-model="newComment"
				placeholder="Write a comment..."
				class="ml-3 p-2 bg-gray-100 rounded-lg flex-grow resize-none"></textarea>
			<button
				@click="addComment"
				class="ml-3 px-4 py-2 bg-blue-600 text-white rounded-lg">
				add
			</button>
		</div>
	</div>
</template>
<script>
	import axios from 'axios';
	import { useUserStore } from '../../stores/user';
	export default {
		name: 'CommentItem',
		props: {
			comments: {
				type: Object,
				required: true,
			},
			postId: {
				type: String,
				required: true,
			},
		},
		emits: ['commentAdded'], // Declare the custom event here
		data() {
			return {
				userStore: useUserStore(),
				newComment: '',
				userHasCommented: false,
			};
		},
		mounted() {
			// Assuming each comment has a 'userId' field to identify the user who commented
			this.userHasCommented = this.comments.some(
				(comment) => comment.author.user.id === this.userStore.user.id
			);
			console.log('isCommented', this.userHasCommented);
		},
		methods: {
			addComment() {
				axios({
					method: 'post',
					url: `/api/v1/posts/${this.postId}/comment`,
					data: {
						content: this.newComment,
						post: this.postId,
					},
				})
					.then((response) => {
						this.$emit('commentAdded');
						this.newComment = '';
						this.userHasCommented = true;
					})
					.catch((error) => {
						console.log(error);
					});
			},
		},
	};
</script>

<style scoped></style>
