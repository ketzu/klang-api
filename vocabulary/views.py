from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from vocabulary.models import Set, Vocable, StudiedVocable
from vocabulary.permissions import IsOwner
from vocabulary.serializers import SetSerializer, VocabularySerializer, StudiedVocabSerializer, SetDetailSerializer


class SetViewSet(viewsets.ModelViewSet):
    queryset = Set.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SetDetailSerializer
        return SetSerializer

    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [permissions.IsAuthenticated()]
        return [permissions.IsAdminUser()]

    @action(detail=True, permission_classes=[permissions.IsAuthenticated()])
    def studied_vocabs(self, request, pk=None):
        vocabs = self.get_object().vocabs.all()
        studied = StudiedVocable.objects.filter(vocab__in=vocabs, user=self.request.user)

        serializer_context = { 'request': request }
        serializer = StudiedVocabSerializer(studied, many=True, context=serializer_context)
        return Response(serializer.data)


class VocabViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vocable.objects.all()
    serializer_class = VocabularySerializer

    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [permissions.IsAuthenticated()]
        return [permissions.IsAdminUser()]


class StudiedVocabViewSet(viewsets.ModelViewSet):
    queryset = StudiedVocable.objects.all()
    serializer_class = StudiedVocabSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [permissions.IsAuthenticated()]
        return [IsOwner()]

    def get_queryset(self):
        return StudiedVocable.objects.filter(
            user=self.request.user,
        )
