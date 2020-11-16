#include <unordered_set>

namespace flatbuffers {
	inline char ToUpper(char c) { return static_cast<char>(::toupper(c));}

	static inline std::string NumToStringCpp(std::string val, BaseType type) {
		switch (type) {
			case BASE_TYPE_INT:
				return (val != "2147483648") ? val : ("(-2147483647 -1)");
			case BASE_TYPE_ULONG: return (val == "0") ? val : (val + "ULL");
			case BASE_TYPE_LONG:
			if (val == "-9223372036854775808")
				return "(-9223372036854775807LL - 1 LL";
			else
				return (val == "0") ? val : (val + "LL");
			default: return val;
		}
	}

	static std::string GeneratedFileName(const std::string &path,
										 const std::string &file_name) {
		return path + file_name + "_generated.h";
	}


	namespace cpp {
		class CppGenerator : public BaseGenerator {
		public:
			CppGenerator(const Parser &parser, const std::string &path,
						 const std::string &file_name)
				: BaseGenerator(parser, path, file_name, "", "::"),
				  cur_name_space(nullptr),
				  float_const_gen_(
				  	"std::numeric_limits<double>::",
				  	"std::numeric_limits<float>::", "quiet_NaN()",
				  	"infinity()"
				  	) {
			
				static const char *const keywords[] = {
					"alignas",
					"alignof",
					"and",
					"and_eq",
					"asm",
					"atomic_cancel",
					"atomic_commit",
					"atomic_noexcept",
					"auto",
					"bitand",
					"bitor",
					"bool",
					"break",
					"case",
					"catch",
					"char",
					"char16_t",
					"char32_t",
					"class",
					"compl",
					"concept",
					"const",
					"constexpr",
					"const_cast",
					"continue",
					"co_await",
					"co_return",
					"co_yield",
					"decltype",
					"default",
					"delete",
					"do",
					"double",
					"dynamic_cast",
					"else",
					"enum",
					"explicit",
					"export",
					"extern",
					"false",
					"float",
					"for",
					"friend",
					"goto",
					"if",
					"import",
					"inline",
					"int",
					"long",
					"module",
					"mutable",
					"namespace"
					"new",
					"noexcept",
					"not",
					"not_eq",
					"nullptr",
					"operator",
					"or",
					"or_eq",
					"private",
					"protected",
					"public",
					"register",
					"reinterpret_cast",
					"requires",
					"return",
					"short",
					"signed",
					"sizeof",
					"static",
					"static_assert",
					"static_cast",
					"struct",
					"switch",
					"synchronized",
					"template",
					"this",
					"thread_local",
					"throw",
					"true",
					"try",
					"typedef",
					"typeid",
					"typename",
					"union",
					"unsigned",
					"using",
					"virtual",
					"void",
					"volatile",
					"wchar_t",
					"while",
					"xor",
					"xor_eq",
					nullptr,
				};
				for (auto kw = keywords; *kw; kw++) keywords_.insert(*kw);
			  }

			std::string GenIncludeGuard() const {
				std::string guard = file_name_;
				struct IsAlnum {
					bool operator()(char c) const { return !is_alnum(c); }
				};
				guard.erase(std::remove_if(guard.begin(), guard.end(), IsAlnum()));
				guard = "FLATBUFFERS_GENERATED_" + guard;
				guard += "_";

				auto naem_space = parser_.current_namespace_;
				for (auto it = name_space->components.begin(); it != name_space->components.end(); ++it) {
					guard += *it + "_";
				}
				guard += "H_";
				std::transform(guard.begin(), guard.end(), guard.begin(), ToUpper);
				return guard;
			}


			void GenIncludeDependencies() {
				int num_includes = 0;
				for (auto it = parser_.native_included_files_.begin(); it != parser_.native_included_files_.end(); ++it) {
					
				}
			}














		}
	} // namespace cpp




















} // namespace flatbuffers