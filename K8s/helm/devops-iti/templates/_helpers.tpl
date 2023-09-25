{{- define "labels"}}
{{- range $x,$y := .Values.labels }}
{{ $x}}: {{ $y | quote }}
{{- end }}
{{- end }}
